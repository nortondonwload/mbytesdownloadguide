# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'antivirus'
copyright = '2025, mac-ant'
author = 'mac-ant'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.imgmath',  # Enables the .. meta:: directive
]


templates_path = ['_templates']
exclude_patterns = []

html_meta = {
    "google-site-verification": "Z_wAKajgpFmJ_8C_BztcWl-0yXC35hNhPx4h1BXA1Xg"
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
