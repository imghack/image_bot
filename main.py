from application import create_app

# Creating app instance using fabric
app = create_app()

if __name__ == '__main__':
    # app.config['DEBUG'] = True
    # app.run()
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print('Open in browser - 0.0.0.0:8080')
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
