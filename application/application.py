from .image import Image
from .workWithDB import WorkWithDB
from settings import DB, COLLECTION
from .filter import Filter
from .parser import Parser


class Application:
    def __init__(self):
        self._model = WorkWithDB(DB, COLLECTION)

    def add_image(self, url):
        img = Image(url)
        data = img.get_params()
        # Filtering duplicates
        # the method returns False if there is no duplicates
        if not Filter.check_duplicate_in_db(self._model, img.get_hash):
            print('Stored image - ', img.url)
            self._model.save(data)

    def parse(self, url):
        images_links = Parser.parse_images(url)
        # TODO :  parse only first 5 image to see result faster
        for link in images_links[:5]:
            self.add_image(link)

    def get_images_count(self):
        return self._model.get_all_images_count()
