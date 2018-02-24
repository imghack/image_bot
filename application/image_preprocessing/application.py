from .image import Image
from .parser import Parser
from application.db.db import save


def add_image(url):
    """ Image adding function, that inserts data into mongoDB
    :param url: the link to download photo
    :return: boolean result of adding image (T OR F)
    """
    img = Image(url)
    data = img.get_params()
    return save(data)


def parse(url, quantity):
    """ Url-parser function, that extracts fixed-size quantity of images from url
        (Insert only unique values)
    :param url: the link to web-site with images
    :param quantity: the quantity of images to insert
    """
    images_links = Parser.parse_images(url)
    quantity = int(quantity)
    # TODO :  parse only first 5 image to see result faster
    while quantity > 0:
        # if the image is duplicated -> pick another one
        quantity = quantity - 1 if add_image(next(images_links)) else quantity
