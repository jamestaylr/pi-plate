#!/usr/bin/python

import tornado.httpserver
import tornado.ioloop
import tornado.web
import threading
import os
import logging

wss = []


class IndexHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.render('../web/index.html')


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [(r'/', IndexHandler)]
        settings = {'debug': True,
                    'static_path': os.path.join(os.path.dirname(__file__),
                    '../web')}
        tornado.web.Application.__init__(self, handlers, **settings)


class ServerThread(threading.Thread):

    def run(self):
        logging.info('Starting server.')

        try:
            http_server = tornado.httpserver.HTTPServer(Application())
            http_server.listen(self._kwargs['PORT'])

            main_loop = tornado.ioloop.IOLoop.instance()

            logging.info('The web server successfully bound to port %d'
                         % self._kwargs['PORT'])

            # starts the main IO loop
            main_loop.start()
            
        except OSError:
            logging.error('The web server failed to bind to the port!')


