#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r", encoding="utf-8") as fd:
    requirements = list(filter(lambda r: not r.strip().startswith("#"), fd.readlines()))

test_requirements = requirements


setup(
    name="vulyk_translations",
    version="0.1.0",
    description="Vulyk translation QE plugin",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Dmytro Chaplynskyi",
    author_email="chaplinsky.dmitry@gmail.com",
    url="https://github.com/lang-uk/vulyk-translations",
    packages=[
        "vulyk_translations",
        "vulyk_translations.models",
        "vulyk_translations.static",
    ],
    package_dir={"vulyk_translations": "vulyk_translations"},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords="vulyk_translations",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    scripts=[],
)
