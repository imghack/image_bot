from flask import Flask, Response, render_template, request, redirect

from application import application
from api import api

# app init
app = Flask(__name__, static_url_path='/', static_folder='static')

# default route
@app.route('/')
def index():
    return render_root_template()


@app.route('/parse', methods=['POST'])
def post():
    if request.method == 'POST':
        # TODO : check is True url / don't believe user
        print(request.form)
        application.parse(request.form['url'], request.form['quantity'])
        return redirect('/')


@app.route("/download/image")
def download_image():
    return Response(application.get_images_as_xml(), mimetype="text/xml",
                    headers={"Content-disposition": "attachment;"})


app.register_blueprint(api, url_prefix='/api')

# helpers
def render_root_template():
    return render_template('index.html', images_count=application.get_images_count())


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
