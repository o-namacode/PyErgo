from setuptools import setup, find_packages
from pathlib import Path
# Get ReadMe for Long Description
with Path('README.md').open('r') as fp:
    long_description = '\n'.join(fp.readlines()) 

setup(
    name="pyergo",
    fullname="PyErgo Python Library",

    description="""
    A collection of frequently reused code for projects.""",
    long_description=long_description or '',

    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
