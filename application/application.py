from .image import Image
from .workWithDB import WorkWithDB
from settings import DB, COLLECTION


class Application:
    def __init__(self):
        self._model = WorkWithDB(DB, COLLECTION)

    def add_image(self, url):
        data = Image(url).get_params()
        print(data)
        self._model.save(data)

    def parse(self, url):
        # parser should be here =)
        self.add_image('static/images/mono.png')

    def get_images_count(self):
        return self._model.get_all_images_count()
