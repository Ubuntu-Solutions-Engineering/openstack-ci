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
Title: Test upstream deb is copied to container properly
Result: Should return 0 if found upstream deb and fail otherwise
"""

import sys
sys.path.insert(0, '/usr/share/openstack')
import pytest
import shlex
from subprocess import call
from unittest.mock import MagicMock
from cloudinstall.single_install import SingleInstall


@pytest.fixture(scope="module")
def container():
    opts = MagicMock()
    opts.upstream_deb = '../openstack_0.21-0ubuntu1_all.deb'
    opts.install_only = True
    install = SingleInstall(opts, MagicMock())
    install.start_task = MagicMock()
    install.stop_current_task = MagicMock()
    install.register_tasks = MagicMock()
    with pytest.raises(SystemExit):
        install.do_install()

    def fin():
        # Cleanup after each test
        call(shlex.split('sudo openstack-install -k'))
    return install
