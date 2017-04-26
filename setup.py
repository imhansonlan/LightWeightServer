#!/usr/bin/env python
# -*- coding: utf-8 -*-
# gen egg: python setup.py bdist_egg
# install: pip install dist/*.egg

from setuptools import setup

setup(
    name="LightWeightServer",
    version="0.1.0",
    packages=['LightWeightServer', ],
    zip_safe=False,

    description="simple http server with tornado.",
    long_description="simple http server with tornado.",
    author="hanson",
    author_email="liangguohuan@gmail.com",

    license="GPL",
    keywords=("lightweight", "server"),
    platforms="Independant",
    url="https://github.com/liangguohuan",
    entry_points={
        'console_scripts': [
            'LightWeightServer = LightWeightServer.__main__:main',
        ],
    },
)
