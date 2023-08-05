# Description: This file is used to install the package

from pathlib import Path
from setuptools import setup

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={"": "Src"},
    py_modules=["moneycontrol_api"],
)
