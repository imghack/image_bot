from flask import Flask, render_template

from application import Application

# app init
app = Flask(__name__)

# default route
@app.route('/')
def index():
    imageApp = Application()
    imageApp.add_image('static/images/mono.png')
    return render_template('index.html')


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
