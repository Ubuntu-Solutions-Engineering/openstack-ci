#!/usr/bin/env python3
# -*- mode: python; -*-
#
# setup.py - MAAS distutils setup
#
# Copyright 2014 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
openstack-ci
============

Ubuntu OpenStack Installer CI

Functional tests for the installer
"""

from setuptools import setup, find_packages

import os
import sys

import openstackci

if sys.argv[-1] == 'clean':
    print("Cleaning up ...")
    os.system('rm -rf openstackci.egg-info build dist')
    sys.exit()

setup(name='openstackci',
      version=openstackci.__version__,
      description="Ubuntu OpenStack Installer CI",
      long_description=__doc__,
      author='Canonical Solutions Engineering',
      author_email='ubuntu-dev@lists.ubuntu.com',
      url='https://github.com/Ubuntu-Solutions-Engineering/openstack-ci',
      license="AGPLv3+",
      scripts=['openstack-ci', 'openstack-ci-web'],
      packages=find_packages(exclude=["test"]),
      data_files=[
          ('share/man/man1', ['man/en/openstack-ci.1'])
      ])
