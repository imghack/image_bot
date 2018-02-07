from flask import Flask
from celery import Celery
from .settings import BACKEND, BROKER

celery = Celery(__name__, broker=BROKER, backend=BACKEND)

from .image_bot import application
from .api import api


def create_app():
    """
        Creation of the app and making the adjustments
    """
    app = Flask(__name__, static_url_path='/image_bot/static')
    celery.conf.update(app.config)

    return app
