# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Laboratórios didáticos de Geoprocessamento"
copyright = "2023, LabGeo - Escola Politécnica da Universidade de São Paulo"
author = "Guilherme Fernandes Alves"
release = "v0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# add support for .ipynb files
extensions = ["nbsphinx", "myst_parser"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".txt"]

language = "pt_BR"
nbsphinx_allow_errors = True
nbsphinx_execute = "never"  # TODO: change to "auto" when ready

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"  # "renku"
html_title = "PTR3311-Python"
html_theme_options = {
    "navigation_with_keys": True,
    "repository_url": "https://github.com/Gui-FernandesBR/PTR3311-Python",
    "launch_buttons": {"colab_url": "https://colab.research.google.com"},
    "path_to_docs": "labs",
    "use_repository_button": True,
    "show_navbar_depth": 2,
    "use_download_button": True,
}
# html_static_path = ["_static"]

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

# latex_engine = "xelatex"
# latex_documents = [
#     (
#         master_doc,
#         "PTR3311-Python.tex",
#         "PTR3311-Python Documentation",
#         "Guilherme",
#         "manual",
#     )
# ]
latex_logo = "static/labgeo-logo.png"

# -- Options for linkcheck ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-linkcheck


# -- Options for GitHub button -----------------------------------------------

html_context = {
    # "github_url": "https://github.com",
    "github_user": "Gui-FernandesBR",
    "github_repo": "PTR3311-Python",
    "github_version": "master",
    "doc_path": "labs",
}

# source_suffix = {
#     ".rst": "restructuredtext",
#     ".md": "markdown",
#     ".ipynb": "nbsphinx",
# }

# source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}

highlight_language = "python3"

html_codeblock_linenos_style = "table"

html_logo = "static/labgeo-logo.png"
html_favicon = "static/logo_minerva.jpg"
html_search_language = "pt_BR"
