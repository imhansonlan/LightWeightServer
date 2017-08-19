#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gen egg: python setup.py bdist_egg
# install: pip install dist/*.egg

from setuptools import setup

PACKAGES_NAME = "LightWeightServer"

setup(
    name=PACKAGES_NAME,
    version="0.1.0",
    zip_safe=False,

    description="simple http server with tornado.",
    long_description="simple http server with tornado.",
    author="hanson",
    author_email="liangguohuan@gmail.com",

    license="GPL",
    keywords=("lightweight", "server"),
    platforms="Independant",
    url="https://github.com/liangguohuan",
    packages=[PACKAGES_NAME, ],
    package_dir={PACKAGES_NAME: "src"},
    entry_points={
        'console_scripts': [
            '%s = %s.__main__:main' % (PACKAGES_NAME, PACKAGES_NAME),
        ],
    },
)
