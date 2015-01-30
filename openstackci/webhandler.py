import tornado.web
import logging
from json import dumps

log = logging.getLogger('openstackci.web')


class Base(tornado.web.RequestHandler):

    @property
    def config(self):
        return self.application.config

    def head(self, *args, **kwargs):
        self.get(*args, **kwargs)
        self.request.body = ''

    def is_argument_present(self, name):
        return not (self.request.arguments.get(name, None) == None)

    # Page render
    def render(self, template_name, **kwargs):
        tornado.web.RequestHandler.render(self,
                                          template_name,
                                          **kwargs)

    # API render
    def render_json(self, content):
        content_json = dumps(content)
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(content_json)
        self.finish()
