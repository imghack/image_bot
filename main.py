
from flask import Response, render_template, request, redirect
from application import application, create_app
from application import api


# Creating app instance using fabric
app = create_app()
app.app_context().push()



# default route
@app.route('/')
def index():
    return render_root_template()


@app.route('/parse', methods=['POST'])
def post():
    if request.method == 'POST':
        # TODO : check is True url / don't believe user
        print(request.form)
        application.parse.delay(request.form['url'], request.form['quantity'])
        return redirect('/parse')
    return render_template("parse.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
         return render_template("about.html")



@app.route("/download/image")
def download_image():
    return Response(application.get_images_as_xml.delay(), mimetype="text/xml",
                    headers={"Content-disposition": "attachment;"})


app.register_blueprint(api, url_prefix='/api')

# helpers
def render_root_template():
    return render_template('index.html', images_count=application.get_images_count())


if __name__ == '__main__':
    # app.config['DEBUG'] = True
    # app.run()
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    print('Open in browser - 0.0.0.0:8080')
    server = pywsgi.WSGIServer(('0.0.0.0', 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
