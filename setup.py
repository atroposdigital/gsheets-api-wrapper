from setuptools import find_packages, setup

setup(name = 'gsheets_api_wrapper',
   version = '0.0.1',
   description = 'A wrapper for the Google API',
   package_dir = {"": "app"},
   packages = find_packages(where= "app"),
   url = 'https://github.com/atroposdigital/gsheets-api-wrapper',
   author = 'Dimitris Gkiokas',
   author_email = 'dimitris@atroposdigital.com',
   license = 'MIT')