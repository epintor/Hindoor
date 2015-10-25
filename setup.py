#!/usr/bin/python
# -*- coding: utf-8 *-*

from setuptools import setup
import os
import sys

setup(
    name='Hindoor',
    version='0.1.4',
    author='Painting Entertainment S.L.',
    author_email='epintor@painting-entertainment.com',
    include_package_data = True,
    scripts=['bin/start_hinterface','bin/start_hlog', 'bin/start_hstats', 'bin/hindebug', 'bin/hindnetwork'],
    url='',
    packages=['hindoor', 'hindoor.modules'],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read(),
)