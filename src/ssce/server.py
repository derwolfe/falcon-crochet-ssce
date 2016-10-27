from __future__ import absolute_import, division, print_function

import time
import json

import crochet

import falcon
import requests

from twisted.internet.threads import deferToThread


# twisted
def blocking_request():
    print('look at me, I\'ve been called')
    resp = requests.get('https://firedamp.herokuapp.com/')
    return resp.json()

def request_in_thread():
    return deferToThread(blocking_request)

# crochet
@crochet.wait_for(10)
def blocking_iface():
    return request_in_thread()

# falcon
class CrochetResource(object):

    def on_get(self, req, resp):
        resp.body = json.dumps(
            blocking_iface()
        )

# the wsgi app
def api():
    api = falcon.API()
    api.add_route('/threaded', CrochetResource())
    return api

# the twisted server
def run_with_twisted():
    crochet.no_setup()

    from twisted.internet import reactor
    from twisted.web.wsgi import WSGIResource
    from twisted.web.server import Site

    wsgi_app = api()
    app = WSGIResource(reactor, reactor.getThreadPool(), wsgi_app)
    reactor.listenTCP(
        interface='0.0.0.0',
        port=8080,
        factory=Site(app)
    )
    reactor.run()


if __name__ == '__main__':
    run_with_twisted()
