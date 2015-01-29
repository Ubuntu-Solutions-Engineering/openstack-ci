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
import pkgutil
import logging
from importlib import import_module
from subprocess import CalledProcessError
from openstackci.report import Reporter
from cloudinstall.juju import JujuState
from macumba import JujuClient

log = logging.getLogger('openstackci')


class TestUnit:

    name = None
    description = None
    # ID of test i.e. agents_started.py is just 'agents_started'
    # for the identifier
    identifier = None
    install_type = None

    def __init__(self, config):
        self.config = config
        self.report = Reporter(self.name,
                               self.description,
                               self.identifier,
                               self.config)

    def can_run(self):
        if self.config.getopt('install_type') == self.install_type:
            return True
        return False

    def authenticate_juju(self):
        try:
            if not len(self.config.juju_env['state-servers']) > 0:
                state_server = 'localhost:17070'
            else:
                state_server = self.config.juju_env['state-servers'][0]
            self.juju = JujuClient(
                url=os.path.join('wss://', state_server),
                password=self.config.juju_api_password)
            self.juju.login()
            self.juju_state = JujuState(self.juju)
            log.info('Authenticated against juju')
        except ConnectionRefusedError as e:
            log.error("Cannot connect to juju: {}".format(e.strerror))
            sys.exit(e.errno)

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

    def __init__(self, config):
        self.config = config

    def _load_test_modules(self, module_dir=None):
        """ loads tests from directories """
        if module_dir is None:
            module_dir = os.path.abspath('.')
        if module_dir not in sys.path:
            sys.path.insert(0, module_dir)
        import quality
        import regressions
        quality_tests = [import_module('quality.' + tname)
                         for (_, tname, _) in
                         pkgutil.iter_modules(quality.__path__)]
        regression_tests = [import_module('regressions.' + tname)
                            for (_, tname, _) in
                            pkgutil.iter_modules(regressions.__path__)]
        return quality_tests + regression_tests

    def get_test(self, test_name):
        for test in self._load_test_modules():
            t = test.__test_class__(self.config)
            if test_name == t.identifier:
                t.authenticate_juju()
                return t

    def run_install(self, install_cmd):
        log.info("Deploying environment.")
        try:
            install_cmd()
        except CalledProcessError as e:
            sys.exit(e.returncode)

    def run_all_tests(self, test_dir=None):
        if not os.path.exists('quality') and not os.path.exists('regressions'):
            raise SystemExit('Unable to find quality and regressions '
                             'directories, make sure you are running this '
                             'from the toplevel openstack-tests directory.')
        for test in self._load_test_modules(test_dir):
            t = test.__test_class__(self.config)
            if t.can_run():
                t.authenticate_juju()
                log.info("Test: {}".format(t.description))
                t.run()
                t.report.save()
                if t.report.final_exit_code != 0:
                    sys.exit(t.report.final_exit_code)

    def run_test(self, test_name):
        """ Runs a single test """
        # add search path in toplevel tests directory that contains
        # both quality/ and regressions/ directories.
        # i.e ~/openstack-tests
        t = self.get_test(test_name)
        log.info("Loading test {}/{}".format(t.name, t.description))
        t.run()
        t.report.save()
        if t.report.final_exit_code != 0:
            sys.exit(t.report.final_exit_code)
