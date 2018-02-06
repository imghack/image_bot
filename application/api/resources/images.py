from flask_restful import Resource
# TODO: db connection should be one for all blueprints
from application.image_bot.mymongo import get_all_images


class Images(Resource):
    def get(self, id):
        return get_all_images()[id]
