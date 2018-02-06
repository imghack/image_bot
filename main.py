from application import create_app

app = create_app()

if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print('Open in browser - 0.0.0.0:8080')
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
