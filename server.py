import json
import os

import cherrypy

from main import Manager


class Server(object):
    def __init__(self):
        self.manager = Manager()

    @cherrypy.expose()
    def index(self):
        with open("static/index.html", "r") as f:
            content = f.read()
        return content

    @cherrypy.expose()
    def filter(self, searchstr="", page_size=10, page_number=1):
        return json.dumps(self.manager.filter_results(searchstr, page_number=page_number, page_size=page_size))


if __name__ == "__main__":
    conf = {
        '/static': {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir': os.getcwd()+'/static'
        }
    }
    cherrypy.quickstart(Server(), '/', conf)