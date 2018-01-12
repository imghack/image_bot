from flask import Flask, render_template

from image_preprocessing import image_preprocessing_page

# app init
app = Flask(__name__)

# register blue prints
app.register_blueprint(image_preprocessing_page, url_prefix="/preimg")

# default route
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
