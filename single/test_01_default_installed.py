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
Test a default installation of OpenStack installer
"""

import sys
sys.path.insert(0, '/usr/share/openstack')
import pytest
import cloudinstall.utils as utils
from fixture import container
from cloudinstall.core import Controller
import os


def test_mount_cloud_install_dir(container):
    """ Is host .cloud-install mounted within container
    """
    ret = utils.container_run('uoi-bootstrap', 'cat /proc/mounts')
    assert '/home/ubuntu/.cloud-install' in ret


def test_mount_ssh_dir(container):
    """ Is host .ssh dir mounted within container
    """
    ret = utils.container_run('uoi-bootstrap', 'cat /proc/mounts')
    assert '/home/ubuntu/.ssh' in ret


def test_juju_home_set(container):
    """ Is juju environments in custom location
    """
    ret = utils.container_run(
        'uoi-bootstrap', 'test -e .cloud-install/environments.yaml && echo 0')
    assert ret == '0'

def test_upstream_deb_exists(container):
    """ Verify that the upstream local deb gets copied
    into the container. Uses check_output to return an
    empty byte string.
    """
    ret = utils.container_run(
        'uoi-bootstrap',
        'test -e .cloud-install/openstack_0.21-0ubuntu1_all.deb && echo 0')
    assert ret == '0'


def test_upstream_installed(container):
    """ Test that the installed openstack version
    is that of the upstream one
    """
    ret = utils.container_run(
        'uoi-bootstrap',
        'dpkg-query -W -f=\'${Version}\' openstack')
    assert ret == '0.21-0ubuntu1'
