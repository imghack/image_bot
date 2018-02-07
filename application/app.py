from flask import Flask, Response, render_template, request, redirect
from flask_socketio import SocketIO

from .image_bot import application
from .api import api
from .logger import Logger
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
        if request.method == 'POST':
            # TODO : check is True url / don't believe user
            print(request.form)
            application.parse(request.form['url'], request.form['quantity'])
            return redirect('/parse')
        return render_template("parse.html")

    @app.route('/images', methods=['GET', 'POST'])
    def about():
        if request.method == 'GET':
            return render_template("images.html", application.get_images_count())

    @app.route("/download/image")
    def download_image():
        logger.send_message('download completed')
        return Response(application.get_images_as_xml(), mimetype="text/xml",
                        headers={"Content-disposition": "attachment;"})

    app.register_blueprint(api, url_prefix='/api')

    # helpers
    def render_root_template():
        return render_template('index.html', images_count=application.get_images_count())
