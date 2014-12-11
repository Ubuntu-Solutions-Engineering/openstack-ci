#!/usr/bin/env python3
#
# Copyright 2014 Canonical, Ltd.
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

"""
Test runner
"""

from subprocess import check_call
import glob
import sys

if __name__ == '__main__':
    for test in sorted(glob.iglob('single/*-test*.py')):
        sys.stdout.write("Running test: {} ...".format(test))
        try:
            check_call([test])
            sys.stdout.write("Ok\n")
        except Exception as e:
            sys.stdout.write("Failed: {}\n".format(e))

        # Cleanup after each test
        try:
            check_call(['single/cleanup.py'])
        except Exception as e:
            sys.stdout.write("Failed to clean environment: {}\n".format(e))
            sys.exit(1)
