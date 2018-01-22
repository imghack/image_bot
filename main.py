from flask import Flask, render_template, request, redirect

from application import Application

# app init
app = Flask(__name__)

imageApp = Application()


# default route
@app.route('/')
def index():
    return render_root_template()


@app.route('/parse', methods=['POST'])
def post():
    if request.method == 'POST':
        # TODO : check is True url / don't belive user
        print(request.form)
        imageApp.parse(request.form['url'])
        return redirect('/')


def render_root_template():
    return render_template('index.html', images_count=imageApp.get_images_count())


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
