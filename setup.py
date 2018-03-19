#!/usr/bin/env python
# encoding UTF-8

from setuptools import setup
from setuptools import find_packages

def readme():
    with open('README.md', 'r') as readme_file:
        return readme_file.read()


setup(
    name='pytest-redmine',
    version='0.0.1',
    license='MIT',
    description='Pytest plugin for redmine',
    long_description= readme(),
    url='https://github.com/matisla/pytest-redmine',
    packages=find_packages('src'),
    package_dir={'':'src'},
    entry_points = {
        'pytest11' : [
            'pytest-redmine = pytest-redmine.plugin',
        ]
    }
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI :: MIT License',
        'Operation System :: Microsoft :: Windows',
        'Operation System :: POSIX',
        'Topic :: Software Developpement :: Testing',
        'Topic :: Utilities',
    ],
    keywords=[
        'redmine', 'pytest', 'py.test'
    ],
    install_requires=[
        'pytest',
        'python-redmine'
    ],
    python_requires='>=3.6',
)
        

