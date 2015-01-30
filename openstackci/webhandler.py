import tornado.web
import logging
from json import dumps
from tornado.escape import to_unicode

log = logging.getLogger('openstackci.web')


class Base(tornado.web.RequestHandler):

    @property
    def config(self):
        return self.application.config

    @property
    def session(self):
        return self.application.session

    def head(self, *args, **kwargs):
        self.get(*args, **kwargs)
        self.request.body = ''

    def get_current_user(self):
        auth = self.get_secure_cookie('userid')
        if not auth:
            return None
        return to_unicode(self.get_secure_cookie('userid'))

    def get_secure_cookie(self, name, if_none=""):
        cook = tornado.web.RequestHandler.get_secure_cookie(self, name)
        if cook is None:
            return if_none
        return cook

    def is_argument_present(self, name):
        return not (self.request.arguments.get(name, None) is None)

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
