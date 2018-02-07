from flask_restful import Resource
# TODO: db connection should be one for all blueprints
from application.db.db import get_all_images


class Images(Resource):
    def get(self, id):
        return get_all_images()[id]
