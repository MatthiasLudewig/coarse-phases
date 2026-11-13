"""Shared mathematical notation for MathJax and the TikZ LaTeX preamble."""

from string import ascii_uppercase


# Names omit the leading backslash; values are ordinary TeX replacements.
MATH_MACROS = {
    **{f"c{letter}": rf"\mathcal{{{letter}}}" for letter in ascii_uppercase},
    **{f"s{letter}": rf"\mathscr{{{letter}}}" for letter in ascii_uppercase},
    **{letter: rf"\mathbb{{{letter}}}" for letter in "NZQRC"},
    **{
        name: rf"\operatorname{{{name}}}"
        for name in (
            "Mat End Hom Aut Inn id Der ind tr str Tr Str supp ch coker spec "
            "colim Var Exp dom ran Loc Az Con CAR Cl Fun Ad ad Tot"
        ).split()
    },
    **{
        name: rf"\mathrm{{{name}}}"
        for name in "BornCoarse Set Cat Ab Grp Vect Hilb Top Sp".split()
    },
}
# Both renderers already supply \ker and \lim. In particular, keep \lim's
# standard display limits instead of redeclaring it as an ordinary operator.

LATEX_PREAMBLE = r"\usepackage{amsmath,amssymb,mathrsfs}" + "\n" + "\n".join(
    rf"\providecommand{{\{name}}}{{{replacement}}}"
    for name, replacement in MATH_MACROS.items()
)
