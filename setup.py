
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'IaaS report api',
    'author': 'Raymond Kristiansen',
    'url': 'https://github.com/norcams/report-app',
    'download_url': 'https://github.com/norcams/report-app',
    'author_email': 'raymond.Kristiansen@uib.no',
    'version': '0.1',
    'install_requires': [
        'flask==1.0.2',
        'connexion==1.5.2',
        'Flask-SQLAlchemy==2.3.2',
        'bcrypt',
        'PyMySQL',
        'Flask-Cors'
    ],
    'packages': ['api', 'oauth'],
    'scripts': [],
    'name': 'report-api'
}

setup(**config)
