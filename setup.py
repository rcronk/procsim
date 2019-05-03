# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='procsim',
    version='0.1.0',
    description='Process Simulator',
    long_description=readme,
    author='Robert Cronk',
    author_email='cronk.r@gmail.com',
    url='https://github.com/rcronk/procsim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
