from flask import Blueprint
from flask_restful import Api

from api.resources.images import Images
from api.resources.images_list import ImagesList

api_blueprint = Blueprint('api', __name__, template_folder='templates')
api = Api(api_blueprint)

api.add_resource(ImagesList, '/images')
api.add_resource(Images, '/images/<int:id>')

