import tornado.httpserver
import tornado.ioloop
import tornado.web
import os
import configparser

PORT = 8080
DEBUG = False

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


def setup_config():
    
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
        PORT = config.getint('DEFAULT', 'port')
        DEBUG = config.getboolean('DEFAULT', 'debug')
        
    except configparser.NoOptionError:
        print('Could not load configuration file!')

setup_config()

print ("Starting server.")
http_server = tornado.httpserver.HTTPServer(Application())
http_server.listen(8080)

# starts the main IO loop
main_loop = tornado.ioloop.IOLoop.instance()
main_loop.start()
