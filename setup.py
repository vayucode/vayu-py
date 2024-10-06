from setuptools import setup, find_packages
from vayu_sdk import __version__
import os

def read_requirements():
    requirements = []
    if os.path.exists('requirements.txt'):
        with open('requirements.txt') as req:
            requirements = req.read().splitlines()
    return requirements

setup(
    name="vayu-py",
    version=__version__,
    packages=find_packages(),
    install_requires=read_requirements(),    
    description="The Vayu API client library in Python",
    author="Fadi Atamny",
    author_email="fadi@withvayu.com",
    url="https://github.com/weft-finance/vayu-py",
)
