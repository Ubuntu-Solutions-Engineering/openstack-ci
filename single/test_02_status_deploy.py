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
Title: Test OpenStack services are deployed
Result: Should return 0 if all services deployed, 1 otherwise.
"""

import sys
sys.path.insert(0, '/usr/share/openstack')
import os.path as path
import pytest
import cloudinstall.utils as utils
from fixture import container
import json
from cloudinstall.core import Controller
from unittest.mock import MagicMock
from cloudinstall.config import Config

cfg = Config()

@pytest.fixture()
def status_start():
    with pytest.raises(SystemExit):
        utils.container_run_status('uoi-bootstrap', 'openstack-status --headless')
    while not path.exists(path.join(cfg.cfg_path, 'finished.json')):
        continue


@pytest.mark.usefixtures('status_start')
def test_status_finish(container):
    """ Verify OpenStack cloud is deployed
    """
    ret = json.loads(utils.slurp(path.join(cfg.cfg_path, 'finished.json')))
    assert ret['status'] == 'success'
