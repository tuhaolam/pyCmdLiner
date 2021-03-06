#!/usr/bin/env python
#
# Copyright 2012 Filippo Pacifici
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pycmdliner",
    version = "0.1.0",
    author = "Filippo Pacifici",
    author_email = "filippo.pacifici@gmail.com",
    description = ("A scaffolding module for command line applications: " +
        "It manages input commands and parameters invoking provided business logic."),
    license = "Apache",
    keywords = "commandline tools scaffolding",
    url = "https://github.com/fpacifici/pyCmdLiner",
    packages=['pycmdliner', 'tests'],
    long_description=read('README.md'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
    ],
)