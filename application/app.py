from flask import Flask, Response, render_template, request, redirect
from flask_socketio import SocketIO

from .image_bot import application
from .db.db import get_all_images
from .api import api
from .utils.logger import Logger
from .forms import ParseForm
from .settings import STATIC_PATH


# def create_app():
#     app = Flask(__name__, static_url_path=STATIC_PATH)
# 
#     setup_routes(app)
# 
#     return app
# 
