from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from .Image import Image

DEFAULT_TEMPLATE = 'image_process'
# TODO : remove absolute link
TEST_IMAGE_URL = 'image_preprocessing/images/test.jpg'

image_preprocessing_page = Blueprint('image_preprocessing_page', __name__, template_folder='templates')

image = Image(TEST_IMAGE_URL)

@image_preprocessing_page.route('/', defaults={'page': DEFAULT_TEMPLATE})
def show(page):
    try:
        return render_template(page + '.html', data=image.get_params())
    except TemplateNotFound:
        abort(404)
