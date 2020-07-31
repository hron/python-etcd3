#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not re.match(r'(\s*#|-r)', line)
        ]


requirements = load_reqs('requirements/base.txt')
test_requirements = load_reqs('requirements/test.txt')

setup(
    name='etcd3aio',
    version='0.1.0',
    description="Python client for the etcd3 API for asyncio",
    long_description=readme,
    author="Aleksei Gusev",
    author_email='aleksei.gusev@gmail.com',
    url='https://github.com/hron/etcd3aio',
    packages=[
        'etcd3aio',
        'etcd3aio.etcdrpc',
    ],
    package_dir={
        'etcd3aio': 'etcd3aio',
        'etcd3aio.etcdrpc': 'etcd3aio/etcdrpc',
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='etcd3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
