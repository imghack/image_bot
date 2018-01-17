from flask import Flask, render_template, request

from application import Application

# app init
app = Flask(__name__)

imageApp = Application()

# default route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # TODO : check is True url / don't belive user
        imageApp.parse(request.form['url'])
        return render_template('index.html', images_count=imageApp.get_images_count())
    else:
        return render_template('index.html', images_count=imageApp.get_images_count())


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
