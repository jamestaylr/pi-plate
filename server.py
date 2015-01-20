import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
 
class MainHandler(tornado.web.RequestHandler):
    def get(self, filename):
        self.render(os.path.join("web/compiled/" + filename))

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'^/(.*)$', MainHandler),
        ]
        settings = {
            "debug": True,
            "static_path": os.path.join(os.path.dirname(__file__), "web")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


application = Application()
""" Defines the server parameters
"""

print ("Starting server.")
http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8080)

# starts the main IO loop
main_loop = tornado.ioloop.IOLoop.instance()
main_loop.start()
