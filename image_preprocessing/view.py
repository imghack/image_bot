from flask import Blueprint, render_template

from application.Image import Image

DEFAULT_TEMPLATE = 'image_process'
# TODO : remove absolute link
TEST_IMAGE_URL = 'static/images/test.jpg'

image_preprocessing_page = Blueprint('image_preprocessing_page', __name__, template_folder='templates')

image = Image(TEST_IMAGE_URL)


@image_preprocessing_page.route('/')
def show():
    return render_template(DEFAULT_TEMPLATE + '.html', data=image.get_params())

