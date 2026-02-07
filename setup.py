"""
The setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools(or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more.

"""

from setuptools import find_packages,setup 


Hyphen_dot = "-e ."

def get_packages(file):

    """
    This function return list of necessary packages from requirements.txt file

    """
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_dot in requirements:
            requirements.remove(Hyphen_dot)
    return requirements

setup(
    name = "Network Security",
    version = "1.0.0",
    author= "Kirti Verma",
    author_email="kv.edu14@gmail.com",
    packages=find_packages(),
    install_requires = get_packages("requirements.txt"),
)