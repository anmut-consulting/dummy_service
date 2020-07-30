#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from typing import List

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

setup_requirements = ["pytest-runner"]  # type: List[str]

test_requirements = ["pytest"]  # type: List[str]

setup(
    author="Jori Geysen",
    author_email="jori.geysen@anmut.co.uk",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    dependency_links=[],
    description="This is a package containing a dummy service, mad. Here, we can explore the functionalities of the libraries we will use to develop wrapper services for different functional areas within Anmut (data condition, assurance reporting, market data valuation, etc.).  ",
    install_requires=["flask", "flask-sqlalchemy", "flask-migrate"],
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="dummy_service",
    name="dummy_service",
    packages=find_packages(include=["dummy_service*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/anmut-consulting/dummy_service",
    version="0.0.1",
    zip_safe=False,
)
