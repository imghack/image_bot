from lxml import html
import requests


class Parser:
    """
    Class for parsing web site
    """
    @staticmethod
    def parse_images(url):
        """
        Parse images from any web site
        :param url: image url
        :return: list of image links
        """
        page = requests.get(url)
        tree = html.fromstring(page.content)

        images = tree.cssselect('img')
        for image in images:
            link = image.get('src')
            if link and link.startswith('http'):
                print('Founded image link', link)
                yield link

