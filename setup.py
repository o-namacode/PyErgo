from setuptools import setup, find_packages
from pathlib import Path

# Get the long description from README.md
with Path('README.md').open('r', encoding='utf-8') as fp:
    long_description = fp.read()

# Get the list of dependencies from requirements.txt, excluding comments and blank lines
with Path('requirements.txt').open('r') as fp:
    install_requires = [
        line.strip() for line in fp.readlines()
        if line.strip() and not line.startswith('#')
    ]

setup(
    name="pyergo",
    fullname="PyErgo Python Library",

    description="""
    A collection of frequently reused code for projects.""",
    long_description=long_description or '',
    long_description_content_type='text/markdown',

    version="0.1.2.5",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
)
