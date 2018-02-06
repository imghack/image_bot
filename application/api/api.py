from flask import Blueprint
from flask_restful import Api

from application.api.resources import Images
from application.api.resources import ImagesList

api_blueprint = Blueprint('api', __name__, template_folder='templates')
api = Api(api_blueprint)

api.add_resource(ImagesList, '/images')
api.add_resource(Images, '/images/<int:id>')

