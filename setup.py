import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'aquosRemote'
DESCRIPTION = 'My short description for my project.'
KEYWORDS = 'aquos tv remote'
URL = 'https://github.com/thehappydinoa/aquosRemote'
EMAIL = 'thehappydinoa@gmail.com'
AUTHOR = 'thehappydinoa'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = '1.5.0'

REQUIRED = []

EXTRAS = {
    'dev': ['twine', 'unittest']
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system(
            '{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["tests", "docs"]),
    project_urls={
        "Bug Reports": "https://github.com/thehappydinoa/aquosRemote/issues",
        "Say Thanks!": "http://saythanks.io/to/thehappydinoa",
        "Contribute!": "https://github.com/thehappydinoa/aquosRemote/pulls",
        "Follow Me!": "https://twitter.com/thehappydinoa/",
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)
