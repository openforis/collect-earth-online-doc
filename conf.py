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

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
#    "sphinx.ext.napoleon",
#    "sphinx.ext.graphviz",
    "sphinxcontrib.images",
    "sphinxcontrib.icon",
    "sphinxcontrib.btn",
    "sphinxcontrib.email",
    "sphinxcontrib.youtube",
    "sphinxcontrib.bibtex",
    "sphinx_design",
#    "sphinx_togglebutton",
#    "sphinx_favicon",
#    "sphinx_last_updated_by_git",
#    "notfound.extension",
    "_extentions.line_break",
#    "_extentions.custom_edit",
    "_extentions.logos",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
email_automode = True


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
    "footer_start": ["copyright", "map", "sphinx-version", "licence"],
    "footer_end": ["community", "issue-tracker", "e-learning", "stackexchange"],
}
