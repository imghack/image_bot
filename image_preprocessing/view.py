from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

DEFAULT_TEMPLATE = 'image_process'

image_preprocessing_page = Blueprint('image_preprocessing_page', __name__, template_folder='templates')


@image_preprocessing_page.route('/', defaults={'page': DEFAULT_TEMPLATE})
def show(page):
    try:
        return render_template(page + '.html')
    except TemplateNotFound:
        abort(404)
