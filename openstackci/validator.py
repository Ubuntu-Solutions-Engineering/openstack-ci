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

log = logging.getLogger('openstackci')


class Validator:

    def __init__(self, config, juju):
        self.config = config
        self.juju_state = juju

    def is_services_started(self):
        """ Returns if all services are started and
        what service failed if any
        """
        started_services = []
        failed_services = []
        services = self.juju_state.services
        for svc in services:
            unit = svc.units[0]
            if 'started' not in unit.agent_state:
                failed_services.append(unit.unit_name)
            else:
                started_services.append(unit.unit_name)

        if len(failed_services) > 0:
            return (False, failed_services)
        else:
            return (True, started_services)
