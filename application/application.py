from .image import Image
from .workWithDB import WorkWithDB
from settings import DB, COLLECTION
from .filter import Filter


class Application:
    def __init__(self):
        self._model = WorkWithDB(DB, COLLECTION)

    def add_image(self, url):
        img = Image(url)
        data = img.get_params()
        print(data)
        # Filtering duplicates
        # the method returns False if there is no duplicates
        if not Filter.check_duplicate_in_db(self._model, img.get_hash):
            self._model.save(data)

    def parse(self, url):
        # parser should be here =)
        self.add_image('static/images/mono.png')

    def get_images_count(self):
        return self._model.get_all_images_count()
