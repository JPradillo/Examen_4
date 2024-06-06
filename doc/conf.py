# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

project = 'Examen Entornos'
copyright = '2024, Jorge Pradillo Hinterberger'
author = 'Jorge Pradillo Hinterberger'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
  'sphinx.ext.intersphinx',
  'sphinx.ext.todo',
  'sphinx.ext.mathjax',
  'sphinx.ext.napoleon',
  'sphinx.ext.autosummary']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# cierre de issue Hola

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
