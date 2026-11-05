"""Exercise reader acceptance criteria against the actual generated website."""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import threading

from bs4 import BeautifulSoup
from playwright.sync_api import expect, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "docs" / "_build" / "html"
SCREENSHOTS = ROOT / "artifacts" / "screenshots"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def check_transclusion():
    reference = BeautifulSoup((HTML / "reference/coarse-space.html").read_text(), "html.parser")
    exposition = BeautifulSoup((HTML / "geometry/coarse-spaces.html").read_text(), "html.parser")
    statement = reference.select_one("#def-coarse-space")
    recall = exposition.select_one(".definition-recall")
    assert statement is not None and recall is not None
    for phrase in ("bornological coarse space", "compatibility"):
        assert phrase in statement.get_text() and phrase in recall.get_text()
    assert not recall.select(".caption-number"), "Repeated definition must be unnumbered"
    assert not exposition.select("#def-coarse-space"), "Only canonical occurrence owns the label"
    assert not (HTML / "_snippets").exists(), "Fragments must not become public pages"
    print("PASS: one canonical target, unnumbered reuse, no standalone snippets", flush=True)


def math_ready(page):
    page.wait_for_function(
        "() => window.MathJax && MathJax.startup && MathJax.startup.promise",
        timeout=45000,
    )
    page.evaluate("() => MathJax.startup.promise")
    expect(page.locator("mjx-container").first).to_be_visible()
    assert page.locator("mjx-merror, [data-mjx-error]").count() == 0


def main():
    check_transclusion()
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(HTML)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    errors = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context(viewport={"width": 1440, "height": 1000})
            page = context.new_page()
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"{base}/index.html")
            expect(page.get_by_role("heading", name="Coarse Geometry and Topological Phases", exact=True)).to_be_visible()
            navigation = page.get_by_role("navigation", name="Wiki navigation")
            expect(navigation.get_by_role("link", name="Coarse maps and equivalences", exact=True)).to_be_visible()
            page.screenshot(path=str(SCREENSHOTS / "home-desktop.png"), full_page=True)

            page.locator("article a[href='geometry/coarse-spaces.html']").first.click()
            expect(page).to_have_url(f"{base}/geometry/coarse-spaces.html")
            math_ready(page)
            page.locator("article a[href='../reference/coarse-space.html#def-coarse-space']").first.click()
            expect(page.locator("#def-coarse-space")).to_be_visible()
            expected_branch = os.environ.get("WIKI_EDIT_BRANCH", "main")
            edit = page.locator("a[href*='github.com/MatthiasLudewig/coarse-phases/edit/']").first
            expect(edit).to_have_attribute(
                "href",
                f"https://github.com/MatthiasLudewig/coarse-phases/edit/{expected_branch}/docs/reference/coarse-space.md",
            )
            print("PASS: article navigation, canonical definition, MathJax, edit link", flush=True)

            page.goto(f"{base}/geometry/coarse-spaces.html")
            page.locator("article a[href='../reference/coarse-maps.html#thm-lattice-line']").first.click()
            expect(page.locator("#thm-lattice-line")).to_be_visible()
            proof = page.locator("details.proof-dropdown")
            expect(proof).to_have_count(1)
            assert not proof.evaluate("element => element.open"), "Proof must start collapsed"
            proof.locator("summary").click()
            assert proof.evaluate("element => element.open"), "Proof must expand on click"
            expect(proof.locator(".proof").first).to_be_visible()
            proof.locator("summary").focus()
            page.keyboard.press("Enter")
            assert not proof.evaluate("element => element.open"), "Proof must toggle by keyboard"
            # Reset scroll and keyboard focus before recording full-page previews.
            page.goto(f"{base}/reference/coarse-maps.html")
            math_ready(page)
            page.screenshot(path=str(SCREENSHOTS / "reference-desktop.png"), full_page=True)
            page.locator("#pst-header").get_by_role("button", name="Color mode", exact=True).click()
            page.locator("#pst-header").get_by_role("button", name="Dark", exact=True).click()
            expect(page.locator("html")).to_have_attribute("data-theme", "dark")
            page.locator("h1").click()
            page.screenshot(path=str(SCREENSHOTS / "reference-dark.png"), full_page=True)
            print("PASS: labelled theorem, collapsed proof, mouse and keyboard toggles", flush=True)

            page.goto(f"{base}/algebras/roe-algebras.html")
            remark = page.locator(".admonition.dropdown")
            button = remark.locator("button.toggle-button")
            expect(button).to_have_attribute("aria-expanded", "false")
            button.click()
            expect(button).to_have_attribute("aria-expanded", "true")
            math_ready(page)
            page.goto(f"{base}/phases/introduction.html")
            math_ready(page)
            page.goto(f"{base}/search.html?q=coarse")
            expect(page.locator("#search-results li").first).to_be_visible(timeout=30000)
            print("PASS: technical remark toggle and search results", flush=True)

            mobile = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, has_touch=True)
            mobile_page = mobile.new_page()
            mobile_page.on("pageerror", lambda error: errors.append(str(error)))
            for path, name in [("index.html", "home-mobile.png"), ("reference/coarse-maps.html", "reference-mobile.png")]:
                mobile_page.goto(f"{base}/{path}")
                if path != "index.html":
                    math_ready(mobile_page)
                assert mobile_page.evaluate(
                    "document.documentElement.scrollWidth <= window.innerWidth + 1"
                ), f"Page overflows the mobile viewport: {path}"
                mobile_page.screenshot(path=str(SCREENSHOTS / name), full_page=True)

            mobile_page.get_by_role("button", name="Site navigation", exact=True).click()
            mobile_nav = mobile_page.get_by_role("navigation", name="Wiki navigation")
            expect(mobile_nav.get_by_role("link", name="Roe algebras", exact=True)).to_be_visible()
            mobile_nav.get_by_role("link", name="Roe algebras", exact=True).click()
            expect(mobile_page).to_have_url(f"{base}/algebras/roe-algebras.html")

            # Native proof dropdown also works with JavaScript disabled.
            plain = browser.new_context(java_script_enabled=False)
            plain_page = plain.new_page()
            plain_page.goto(f"{base}/reference/coarse-maps.html")
            plain_proof = plain_page.locator("details.proof-dropdown")
            plain_proof.locator("summary").click()
            expect(plain_proof.locator(".proof").first).to_be_visible()
            assert not errors, f"Browser script errors: {errors}"
            print("PASS: mobile layout, proof without JavaScript, no script errors", flush=True)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
