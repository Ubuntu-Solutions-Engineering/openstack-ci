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
Title: Default installation of single installer
Result: Should return 0 if successful and fail otherwise
"""

import sys
sys.path.insert(0, '/usr/share/openstack')

import pytest
from unittest.mock import MagicMock
from cloudinstall.single_install import SingleInstall


def test_default_install():
    opts = MagicMock()
    opts.install_only = True
    install = SingleInstall(opts, MagicMock())
    install.start_task = MagicMock()
    install.stop_current_task = MagicMock()
    install.register_tasks = MagicMock()
    with pytest.raises(SystemExit):
        install.do_install()