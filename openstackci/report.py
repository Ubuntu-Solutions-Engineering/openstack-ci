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

import logging
import yaml
import os
from datetime import datetime
import cloudinstall.utils as utils


log = logging.getLogger('openstackci')


class Reporter:

    def __init__(self, name, description):
        self.failed_tests = []
        self.success_tests = []
        self.name = name
        self.description = description
        self.now = datetime.now()
        self.final_exit_code = 0

    def fail(self, msg):
        """ Returns a failed message """
        log.error("Result: [FAIL] {}".format(msg))
        self.failed_tests.append(msg)

    def success(self, msg):
        """ Return success message """
        log.info("Result: [PASS] {}".format(msg))
        self.success_tests.append(msg)

    def gen_report(self):
        data = {'timestamp': self.now.isoformat(),
                'name': self.name,
                'description': self.description,
                'num_success': len(self.success_tests),
                'num_failed': len(self.failed_tests)}
        if len(self.failed_tests) > 0:
            self.final_exit_code = 1
            data['status'] = {'text': 'Failed.', 'code': self.final_exit_code}
        elif len(self.success) <= 0:
            self.final_exit_code = 2
            data['status'] = {'text': 'Unknown', 'code': self.final_exit_code}
        else:
            data['status'] = {'text': 'Passed', 'code': self.final_exit_code}
        return data

    def save(self, test_name):
        save_path = os.path.join(utils.install_user(),
                                 '.cloud-install/reports')
        save_file = os.path.join(save_path,
                                 test_name,
                                 '_',
                                 self.now.isoformat())
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        utils.spew(save_file,
                   yaml.safe_dump(self.gen_report(), default_flow_style=False))
        log.info("Report saved: {}".format(save_file))
