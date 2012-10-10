#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='pyiptools',
    author='Nadeem Douba',
    version='0.1',
    author_email='ndouba@gmail.com',
    description='IP address manipulation and ARIN whois lookup library.',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    install_requires=[],
    dependency_links=[]
)


