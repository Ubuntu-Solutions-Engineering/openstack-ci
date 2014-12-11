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

import sys
sys.path.insert(0, '/usr/share/openstack')

from contextlib import contextmanager
from unittest.mock import MagicMock
from cloudinstall.single_install import SingleInstall
from cloudinstall.multi_install import MultiInstall


opts = MagicMock()


@contextmanager
def single_stub():
    install = SingleInstall(opts, MagicMock())
    yield


@contextmanager
def multi_stub():
    return MultiInstall(opts, MagicMock())
