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
    import tornado
    import tornado.httpserver
    import tornado.wsgi

    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.getcwd() + '/static'
        }
    }

    # our WSGI application
    # wsgiapp = cherrypy.tree.mount(Server(), config=conf)
    #
    # # Disable the autoreload which won't play well
    # cherrypy.config.update({'engine.autoreload.on': False})
    #
    # # let's not start the CherryPy HTTP server
    # cherrypy.server.unsubscribe()
    #
    # # use CherryPy's signal handling
    # cherrypy.engine.signals.subscribe()
    #
    # # Prevent CherryPy logs to be propagated
    # # to the Tornado logger
    # cherrypy.log.error_log.propagate = False
    #
    # # Run the engine but don't block on it
    # cherrypy.engine.start()
    #
    # # Run thr tornado stack
    # container = tornado.wsgi.WSGIContainer(wsgiapp)
    # http_server = tornado.httpserver.HTTPServer(container)
    # http_server.listen(os.environ.get("PORT", 8080))
    # # Publish to the CherryPy engine as if
    # # we were using its mainloop
    # tornado.ioloop.PeriodicCallback(lambda: cherrypy.engine.publish('main'), 100).start()
    # tornado.ioloop.IOLoop.instance().start()
