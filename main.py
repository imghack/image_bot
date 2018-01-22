from flask import Flask, render_template, request, redirect

from application import application

# app init
app = Flask(__name__)


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


def render_root_template():
    return render_template('index.html', images_count= application.get_images_count())


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
