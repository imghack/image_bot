from .image import Image
from .parser import Parser
from application.db.db import save

def parse(url, quantity):
    """ Url-parser function, that extracts fixed-size quantity of images from url
        (Insert only unique values)
    :param url: the link to web-site with images
    :param quantity: the quantity of images to insert
    """
    images_links = Parser.parse_images(url)
    quantity = int(quantity)

    for _ in range(0, quantity):
        _store_image(images_links)

def _store_image(images_links):
    image_params = Image(next(images_links)).get_params()
    store_status = save(image_params)
    if not store_status:
        _store_image(images_links)
