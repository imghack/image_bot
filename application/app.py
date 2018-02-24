from flask import Flask
from flask_socketio import SocketIO

from .routes import setup_routes
from .utils.logger import Logger
from .settings import STATIC_PATH


def create_app():
    app = Flask(__name__, static_url_path=STATIC_PATH)
    socketio = SocketIO(app)
    logger = Logger(socketio)

    setup_routes(app, logger)

    return app

