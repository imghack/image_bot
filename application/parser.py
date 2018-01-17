from lxml import html
import requests


def parse_images(url):
    """
    Parse all images from
    """
    page = requests.get(url)
    tree = html.fromstring(page.content)

    links = []
    images = tree.cssselect('img')
    print(images)
    for image in images:
        link = image.get('src')
        if link and link.startswith('http'):
            links.append(link)

    return links
