# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Patch the system path so sphinx can find the source code
import sys
from pathlib import Path

sys.path.insert(0, str(Path('../..', 'src').resolve()))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'testme'
copyright = '2026, Kristoffer A. Wright'
author = 'Kristoffer A. Wright'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc"
]

#templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_theme_options = {
    "bgcolor": "Ivory",
    "headbgcolor": "AntiqueWhite",
    "sidebarbgcolor": "#400000",
    "sidebartextcolor": "Ivory",
    "sidebarlinkcolor": "Ivory",
    "footerbgcolor": "#300000",
    "footertextcolor": "Ivory",
    "relbarbgcolor": "#300000",
    "relbartextcolor": "Ivory",
    "linkcolor": "#A00000",
    "visitedlinkcolor": "#600080",
    "bodyfont": "Garamond",
    "headfont": "Georgia",
    "headtextcolor": "#400000",
    "headlinkcolor": "#400000",
    "codebgcolor": "MistyRose",
    "codetextcolor": "Black"
}
html_static_path = ['_static']
pygments_style = "gruvbox-light"
