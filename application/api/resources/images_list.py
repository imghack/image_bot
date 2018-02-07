from flask_restful import Resource
# TODO: db connection should be one for all blueprints
from application.db.db import get_all_images


class ImagesList(Resource):
    def get(self):
        return get_all_images()
