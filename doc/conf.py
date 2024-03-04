import os


# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MALIN"
copyright = "2024, Vincent Jacques"
author = "Vincent Jacques"
release = os.environ["GABBY_VERSION"]


# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = []

language = "fr"


# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
html_logo = "../frontend/public/logo-cartable-fantastique.png"
