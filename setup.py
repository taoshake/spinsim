#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.0.1"

long_description = """ spinsim: spin simulation software for spin systems using Heisenberg model """

setup(
    name='spinsim',
    version=__version__,
    description=long_description,
    long_description=long_description,
    author='Jiahui Jia',
    author_email='vivian.jiajiahui@gmail.com',
    license='BSD-2-clause',
    packages=find_packages(),
    scripts=[
    ],
    install_requires=['numpy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: BSD License',
    ],
    python_requires='>=3.6',
)
