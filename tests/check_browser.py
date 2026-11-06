"""Check the real site, then isolated article/theorem interaction fixtures."""

from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import threading

from playwright.sync_api import expect, sync_playwright
from support import ARTICLE, THEOREM, WITHOUT_PROOF, build, fixture_source


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'docs' / '_build' / 'html'
SCREENSHOTS = ROOT / 'artifacts' / 'screenshots'


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def serve(directory):
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(directory)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def math_ready(page):
    page.wait_for_function(
        '() => window.MathJax && MathJax.startup && MathJax.startup.promise',
        timeout=45000,
    )
    page.evaluate('() => MathJax.startup.promise')
    expect(page.locator('mjx-container').first).to_be_visible()
    assert page.locator('mjx-merror, [data-mjx-error]').count() == 0


def check_site(browser, errors):
    with serve(HTML) as base:
        context = browser.new_context(viewport={'width': 1440, 'height': 1000})
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(f'{base}/index.html')
        expect(page.get_by_role('heading', name='Coarse Geometry and Topological Phases', exact=True)).to_be_visible()
        navigation = page.get_by_role('navigation', name='Wiki navigation')
        guide = navigation.get_by_role('link', name='Writing and reviewing articles', exact=True)
        expect(guide).to_be_visible()
        page.screenshot(path=str(SCREENSHOTS / 'home-desktop.png'), full_page=True)
        guide.click()
        expect(page).to_have_url(f'{base}/about/authoring.html')
        edit = page.locator("a[href*='github.com/MatthiasLudewig/coarse-phases/edit/']").first
        branch = os.environ.get('WIKI_EDIT_BRANCH', 'main')
        expect(edit).to_have_attribute(
            'href', f'https://github.com/MatthiasLudewig/coarse-phases/edit/{branch}/docs/about/authoring.md'
        )
        page.screenshot(path=str(SCREENSHOTS / 'authoring-desktop.png'), full_page=True)
        page.locator('#pst-header').get_by_role('button', name='Color mode', exact=True).click()
        page.locator('#pst-header').get_by_role('button', name='Dark', exact=True).click()
        expect(page.locator('html')).to_have_attribute('data-theme', 'dark')
        page.locator('h1').click()
        page.screenshot(path=str(SCREENSHOTS / 'authoring-dark.png'), full_page=True)
        page.goto(f'{base}/search.html?q=articles')
        expect(page.locator('#search-results li').first).to_be_visible(timeout=30000)

        mobile = browser.new_context(viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
        mobile_page = mobile.new_page()
        mobile_page.on('pageerror', lambda error: errors.append(str(error)))
        for path, name in [('index.html', 'home-mobile.png'), ('about/authoring.html', 'authoring-mobile.png')]:
            mobile_page.goto(f'{base}/{path}')
            assert mobile_page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'), path
            mobile_page.screenshot(path=str(SCREENSHOTS / name), full_page=True)
        mobile_page.get_by_role('button', name='Site navigation', exact=True).click()
        nav = mobile_page.get_by_role('navigation', name='Wiki navigation')
        nav.get_by_role('link', name='Bibliography', exact=True).click()
        expect(mobile_page).to_have_url(f'{base}/bibliography/index.html')
        context.close()
        mobile.close()
        print('PASS: real site navigation, edit URL, search, dark mode, mobile layout', flush=True)


def check_mathematical_pages(browser, errors):
    # Build separately from docs/_build/html: no fixtures enter the preview artifact.
    with fixture_source() as source, serve(build(source)) as base:
        context = browser.new_context(viewport={'width': 1440, 'height': 1000})
        page = context.new_page()
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(f'{base}/{THEOREM}.html')
        page.locator("article a[href='../articles/ci-object.html#def-ci-object']").click()
        expect(page).to_have_url(f'{base}/{ARTICLE}.html#def-ci-object')
        expect(page.locator('#def-ci-object')).to_be_visible()
        expect(page.get_by_role('heading', name='Fixture article', exact=True)).to_be_visible()
        expect(page.get_by_role('heading', name='Further discussion', exact=True)).to_be_visible()
        expect(page.locator('#thm-ci-inline')).to_have_count(1)
        expect(page.locator('.proof')).not_to_have_count(0)
        math_ready(page)
        page.locator("article a[href='../theorems/ci-result.html#thm-ci-result']").click()
        expect(page).to_have_url(f'{base}/{THEOREM}.html#thm-ci-result')
        expect(page.locator('#thm-ci-result')).to_be_visible()
        expect(page.locator('#lem-ci-step')).to_have_count(1)
        expect(page.locator('#def-ci-object')).to_have_count(0)
        proof = page.locator('details.proof-dropdown')
        expect(proof).to_have_count(1)
        assert not proof.evaluate('element => element.open')
        proof.locator('summary').click()
        assert proof.evaluate('element => element.open')
        expect(proof.locator('.proof').first).to_be_visible()
        proof.locator('summary').focus()
        page.keyboard.press('Enter')
        assert not proof.evaluate('element => element.open')
        math_ready(page)

        page.goto(f'{base}/{ARTICLE}.html')
        remark = page.locator('.admonition.dropdown')
        button = remark.locator('button.toggle-button')
        expect(button).to_have_attribute('aria-expanded', 'false')
        button.click()
        expect(button).to_have_attribute('aria-expanded', 'true')
        page.locator("article a[href='../theorems/ci-statement.html#thm-ci-statement']").click()
        expect(page).to_have_url(f'{base}/{WITHOUT_PROOF}.html#thm-ci-statement')
        expect(page.locator('#thm-ci-statement')).to_be_visible()
        expect(page.locator('details.proof-dropdown')).to_have_count(0)
        expect(page.get_by_text('No proof is supplied on this test-only page.', exact=True)).to_be_visible()
        math_ready(page)

        plain = browser.new_context(java_script_enabled=False)
        plain_page = plain.new_page()
        plain_page.goto(f'{base}/{THEOREM}.html')
        plain_proof = plain_page.locator('details.proof-dropdown')
        plain_proof.locator('summary').click()
        expect(plain_proof.locator('.proof').first).to_be_visible()
        context.close()
        plain.close()
        print('PASS: whole-article definition links; standalone results with/without proofs; inline results; lemma links; MathJax; proof toggles', flush=True)


def check_article_collection(browser, errors):
    """Exercise the actual drafts, including their TeX and review warnings."""
    documents = sorted((ROOT / 'docs' / 'articles').glob('*.md'))
    documents += sorted((ROOT / 'docs' / 'theorems').glob('*.md'))
    warning = 'Agent-generated, not reviewed yet'
    screenshots = {'coarse-space', 'coarse-index', 'controlled-derivations-locally-generated'}
    with serve(HTML) as base:
        for width, height, mode in [(1440, 1000, 'desktop'), (390, 844, 'mobile')]:
            context = browser.new_context(viewport={'width': width, 'height': height})
            page = context.new_page()
            page.on('pageerror', lambda error: errors.append(str(error)))
            for source in documents:
                path = source.relative_to(ROOT / 'docs').with_suffix('.html').as_posix()
                page.goto(f'{base}/{path}')
                expect(page.locator('article h1')).to_be_visible()
                if warning in source.read_text():
                    expect(page.locator('article .warning').get_by_text(warning, exact=True)).to_be_visible()
                if page.locator('article .math').count():
                    math_ready(page)
                assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1'), path
                if source.stem in screenshots:
                    page.screenshot(path=str(SCREENSHOTS / f'{source.stem}-{mode}.png'), full_page=True)

            # Check a real definition link loads its owning article, then a
            # real result link loads its separate statement and proof.
            page.goto(f'{base}/theorems/controlled-derivations-locally-generated.html')
            page.locator("article a[href='../articles/controlled-derivation.html#def-controlled-derivation']").click()
            expect(page).to_have_url(f'{base}/articles/controlled-derivation.html#def-controlled-derivation')
            expect(page.locator('#def-controlled-derivation')).to_be_visible()
            page.locator("article a[href^='../theorems/controlled-derivations-locally-generated.html']").click()
            expect(page.locator('#thm-controlled-locally-generated')).to_be_visible()
            expect(page.get_by_role('heading', name='Construction of the interaction', exact=True)).to_be_visible()
            context.close()
    print(f'PASS: {len(documents)} mathematical pages on desktop and mobile; review warnings; MathJax; actual definition and theorem links', flush=True)


def main():
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            check_site(browser, errors)
            check_article_collection(browser, errors)
            check_mathematical_pages(browser, errors)
            assert not errors, f'Browser script errors: {errors}'
        finally:
            browser.close()


if __name__ == '__main__':
    main()
