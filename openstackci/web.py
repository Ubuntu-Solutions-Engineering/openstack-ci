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
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.process import fork_processes, task_id
from openstackci import webview

log = logging.getLogger('openstackci.web')


class App:

    def __init__(self, config):
        self.config = config
        self.port = self.config.getopt('port')

    def run(self):
        if not self.config.getopt('debug'):
            fork_processes(None)
        self.port += task_id() or 0

        log.info("Starting openstackci web interface "
                 "@ http://localhost:{}".format(self.port))
        tornado.httpserver.HTTPServer(
            Application(self.config)).listen(self.port, '0.0.0.0')
        ioloop = tornado.ioloop.IOLoop.instance()
        if self.config.getopt('debug'):
            tornado.autoreload.start(ioloop)
        ioloop.start()


class Application(tornado.web.Application):

    def __init__(self, config):
        self.config = config

        urls = [(r"/", webview.Index)]
        ui_modules_map = {}
        settings = dict(
            template_path=None,
            static_path=None,
            xsrf_cookies=False if self.config.getopt('debug') else True,
            cookie_secret=self.config.getopt('cookie_secret'),
            debug=self.config.getopt('debug'),
            ui_modules=ui_modules_map)
        tornado.web.Application.__init__(self, urls, **settings)
