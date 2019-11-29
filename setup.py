#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import platform
import os

NAME = 'b0mb3r'
DESCRIPTION = 'Открытый и бесплатный СМС бомбер'
URL = 'https://github.com/crinny/b0mb3r'
EMAIL = ''
AUTHOR = 'crinny'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '2.0.0'

REQUIRED = [
    "httpx", "starlette", "aiofiles", "jinja2", "python-multipart", "fake_useragent", "uvicorn", "click",
]

if platform.system() == "Linux":
    os.system("pkg install build-essential")

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['b0mb3r'],

    entry_points={
        'console_scripts': ['b0mb3r=b0mb3r.__main__:main'],
    },
    install_requires=REQUIRED,
    extras_require={},
    package_data = {
        'b0mb3r': ['static/*', 'templates/*', 'services/*']
    },
    license='Mozilla Public License 2.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
