#
# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from importlib import import_module
from openstackci.report import Reporter


class TestUnit:

    name = None
    description = None

    def __init__(self):
        self.report = Reporter()

    @classmethod
    def name(cls):
        if cls.name:
            return cls.name.lower()
        return cls.__name__.lower()

    @classmethod
    def description(cls):
        if cls.description:
            return cls.description
        return "No description given."

    def run(self):
        """ not implemented """
        pass


class Tester:

    def __init__(self):
        self.test_units = []

    def add_unit(self, test_unit):
        self.test_units.append(test_unit)

    def run_install(self, install_cmd):
        ret = install_cmd()
        if ret['status'] != 0:
            sys.exit(ret['status'])

    def run_test(self, test_name):
        """ Runs a single test """
        # add search path in toplevel tests directory that contains
        # both quality/ and regressions/ directories.
        # i.e ~/openstack-tests
        sys.path.insert(0, os.path.dirname(test_name))
        t = import_module(test_name)()
        t.run()
