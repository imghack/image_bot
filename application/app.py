from flask import Flask, Response, render_template, request, redirect
from flask_socketio import SocketIO

from .image_bot import application
from .db.db import get_all_images
from .api import api
from .utils.logger import Logger
from .forms import ParseForm
from .settings import STATIC_PATH


def create_app():
    app = Flask(__name__, static_url_path=STATIC_PATH)

    setup_routes(app)

    return app

def setup_routes(app):
    socketio = SocketIO(app)
    logger = Logger(socketio)

    # default route
    @app.route('/')
    def index():
        return render_root_template()

    @app.route('/parse', methods=['GET', 'POST'])
    def post():
        form = ParseForm(request.form)
        if request.method == 'POST' and form.validate():
            application.parse(form.url.data, form.quantity.data)
            return render_root_template()
        return render_root_template()

    @app.route('/images', methods=['GET'])
    def about():
        if request.method == 'GET':
            return render_template("images.html", images=get_all_images())

    @app.route("/download/image")
    def download_image():
        logger.send_message('download completed')
        return Response(application.get_images_as_xml(), mimetype="text/xml",
                        headers={"Content-disposition": "attachment;"})

    app.register_blueprint(api, url_prefix='/api')

    # helpers
    def render_root_template():
        return render_template('index.html', images_count=application.get_images_count())
