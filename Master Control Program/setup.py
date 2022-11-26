try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Paul Ambrose',
    'url': 'URL to get at it',
    'download_url': 'where to download it',
    'author_email': 'pablo_rose34@hotmail.com',
    'version': '0.1',
    'install_requires': 'module names',
    'packages': '[NAME]',
    'scripts': 'projectname'

}

setup(**config)
