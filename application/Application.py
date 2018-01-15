from .Image import Image
from .ImageMongoSaver import ImageMongoSaver
from settings import DB, COLLECTION


class Application:
    def __init__(self):
        self._model = ImageMongoSaver(DB, COLLECTION)

    def add_image(self, url):
        data = Image(url).get_params()
        print(data)
        self._model.save(data)
