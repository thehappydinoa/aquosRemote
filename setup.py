from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aquosRemote",
    version="1.4.1",
    description="A small Python module for sending Remote Control Codes to your Sharp AQUOS Smart TV",
    long_description=long_description,
    url="https://github.com/thehappydinoa/aquosRemote",
    author="Aidan Holland (thehappydinoa)",
    author_email="thehappydinoa@gmail.com",

    keywords="aquos tv remote",

    packages=find_packages(exclude=["contrib", "docs", "tests"]),

    project_urls={
        "Bug Reports": "https://github.com/thehappydinoa/aquosRemote/issues",
        "Say Thanks!": "http://saythanks.io/to/thehappydinoa",
        "Contribute!": "https://github.com/thehappydinoa/aquosRemote/pulls",
        "Follow Me!": "https://twitter.com/thehappydinoa/",
    },

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
