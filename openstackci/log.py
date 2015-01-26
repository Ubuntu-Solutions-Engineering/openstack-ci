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

""" Logging interface
"""

from __future__ import unicode_literals
import logging
import pprint


class PrettyLog():

    def __init__(self, obj):
        self.obj = obj

    def __repr__(self):
        return pprint.pformat(self.obj)


def setup_logger(name=__name__):
    """setup logging

    :params str name: logger name
    :returns: a log object

    """
    consolelog = logging.StreamHandler()
    consolelog.setLevel(logging.INFO)
    consolelog.setFormatter(logging.Formatter(
        '[%(levelname)-5s \N{BULLET} %(asctime)s \N{BULLET} %(name)-16s] '
        '%(message)s',
        datefmt='%H:%M:%S'))

    # f = logging.Filter(name='cloudinstall')
    # consolelog.addFilter(f)
    f = logging.Filter(name='openstackci')
    consolelog.addFilter(f)
    logger = logging.getLogger('')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(consolelog)

    return logger
