# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Collect Earth Online'
copyright = '2023, Collect Earth Online team'
author = 'Collect Earth Online team'
release = 'v 0.5'

# -- Path setup ----------------------------------------------------------------
import sys, os
from pathlib import Path

sys.path.append(str(Path(".").resolve()))
sys.path.append(os.path.abspath('_extensions'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.graphviz",
    "sphinxcontrib.images",
    "sphinxcontrib.icon",
    "sphinxcontrib.btn",
    "sphinxcontrib.email",
    "sphinxcontrib.youtube",
    "sphinxcontrib.bibtex",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_favicon",
    "sphinx_last_updated_by_git",
#    "notfound.extension",
    "line_break",
    "custom_edit",
    "logos"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
locale_dirs = ["_locale/"]
gettext_compact = False
language = "en"



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_last_updated_fmt = None
html_sidebars = {"index": []}
html_context = {
    "github_user": "openforis",
    "github_repo": "collect-earth-online-doc",
    "github_version": "main",
    "doc_path": "docs/source",
    "default_mode": "auto",
}
html_static_path = ['_static']
html_css_files = ["css/custom.css", "https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"]
html_js_files = ["https://unpkg.com/leaflet@1.7.1/dist/leaflet.js", "js/custom.js"]

# -- Option for Latex output ---------------------------------------------------

youtube_cmd = (
    r"\newcommand{\sphinxcontribyoutube}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    + "\n"
)
vimeo_cmd = (
    r"\newcommand{\sphinxcontribvimeo}[3]{\begin{figure}\sphinxincludegraphics{{#2}.jpg}\caption{\url{#1#2#3}}\end{figure}}"
    + "\n"
)

latex_elements = {"preamble": youtube_cmd + vimeo_cmd}


# -- Option for the pydata-sphinx-theme ----------------------------------------

html_theme_options = {
    "logo": {
        "image_light": "_static/ceo-logo.png",
        "image_dark": "_static/ceo-logo.png",
    },
    "header_links_before_dropdown": 7,
    "navigation_with_keys": False,
    "show_nav_level": 1,
    "show_prev_next": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/openforis/collect-earth-online",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/OpenForis",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/open-foris/",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "Youtube",
            "url": "https://www.youtube.com/playlist?list=PLiEp-2s05SCwn6LvO7xtdFs-fgHfPrY_e",
            "icon": "fa-brands fa-youtube",
        },
    ],
    "use_edit_page_button": True,
    "article_footer_items": ["last-updated"],
    "footer_start": ["copyright", "sphinx-version", "licence"],
    "footer_end": ["community", "issue-tracker", "e-learning", "stackexchange"],
}

# -- option for the favicon extention ------------------------------------------

favicons = [
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    {"href": "favicon-32x32.png"},
    {"href": "favicon-16x16.png"},
#    {"rel": "mask-icon", "href": "safari-pinned-tab.svg", "color": "#186691"},
]

# -- Options for images --------------------------------------------------------

images_config = {"download": False}


# -- Options for bibtex --------------------------------------------------------

bibtex_bibfiles = ["_bib/ceobib.bib"]
bibtex_reference_style = "author_year"