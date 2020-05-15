# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
# from django.conf import settings
# settings.configure()
import django
sys.path.insert(0, os.path.join(os.path.abspath('.'), '../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "makeIdeasMakeReality.settings")
# After you’ve either set DJANGO_SETTINGS_MODULE or called configure(), you’ll need to call
# django.setup() to load your settings. Calling django.setup() is only necessary if your code is
# truly standalone.
django.setup()


# -- Project information -----------------------------------------------------

project = 'MakeIdeasMakeReality'
copyright = '2020, Niel Godfrey Ponciano'
author = 'Niel Godfrey Ponciano'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme
extensions = [
    'sphinx_rtd_theme', # the theme worked even without this, probably not needed
    'sphinx.ext.autodoc', # get and render documentations written in code
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme' # https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']