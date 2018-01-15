from flask import Flask, render_template

from application import Application

# app init
app = Flask(__name__)

imageApp = Application()

# default route
@app.route('/')
def index():
    imageApp.parse('http://example.com')
    return render_template('index.html', images_count=imageApp.get_images_count())


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
