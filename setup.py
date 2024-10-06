from setuptools import setup, find_packages
from vayu_sdk import __version__

def read_requirements():
    with open('requirements.txt') as req:
        return req.read().splitlines()

setup(
    name="vayu-py",
    version=__version__,
    packages=find_packages(),
    install_requires=read_requirements(),    
    install_requires=[],
    description="The Vayu API client library in Python",
    author="Fadi Atamny",
    author_email="fadi@withvayu.com",
    url="https://github.com/weft-finance/vayu-py",
)