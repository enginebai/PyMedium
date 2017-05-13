#!/usr/bin/python
# -*- encoding: utf-8 -*-

from setuptools import setup

setup(
    name='PyMedium',
    version='1.0.3',
    packages=['pymedium', ],
    license='The MIT License (MIT) Copyright © 2017 Engine Bai.',
    description='PyMedium - Unofficial Medium API',
    long_description=open('README', 'r').read(),
    author='Engine Bai',
    author_email='enginebai@gmail.com',
    url='https://github.com/enginebai/PyMedium',
    install_requires=[
        'flask',
        'bs4',
        'requests',
        'selenium'
      ],
)
