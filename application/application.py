from .image import Image
from .parser import Parser
from .mymongo import save, get_all_images_count


class Application:
    def __init__(self):
        ...

    def add_image(self, url):
        img = Image(url)
        data = img.get_params()
        print('Stored image - ', img.url)
        return save(data)

    def parse(self, url, quantity):
        images_links = Parser.parse_images(url)
        quantity = int(quantity)
        # TODO :  parse only first 5 image to see result faster
        while quantity > 0:
            # if the image is duplicated -> pick another one
            quantity = quantity - 1 if self.add_image(images_links.__next__()) else quantity


    def get_images_count(self):
        return get_all_images_count()