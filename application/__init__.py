from .image import Image
from .parser import Parser
from application import mymongo
from flask import Flask
from settings import BACKEND, BROKER
from celery import Celery

celery = Celery(__name__, broker=BROKER, backend=BACKEND)


def create_app():
    """
        Creation of the app and making the adjustments
    """
    app = Flask(__name__, static_url_path='/image_bot/static')
    celery.conf.update(app.config)
    return app

