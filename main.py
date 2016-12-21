__author__ = 'lorenzo (modified by yukoga)'

import falcon
import os.path as path
from jinja2 import Environment, FileSystemLoader


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        tpl = load_template('things.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text_html'
        resp.body = tpl.render({'message': 'Hello Falcon and Jinja2!! 日本語も'})


things = ThingsResource()
api = falcon.API()
api.add_route('/things', things)

def load_template(template_name):
    ROOT = path.abspath(path.dirname(__file__))
    TEMP_DIR = '/'.join((ROOT, 'templates'))
    env = Environment(loader=FileSystemLoader(TEMP_DIR))
    return env.get_template(template_name)

