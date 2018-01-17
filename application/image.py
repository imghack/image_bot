import imagehash
import requests
import io

from PIL import Image as Img

# Limit of max image colors
# TODO : change to 2 ** 48 fix OverflowError: signed integer is greater than maximum
MAX_COLORS = 2 ** 24


class Image:
    """
    Class for pre-processing image parameters
    """
    def __init__(self, url):
        # TODO : added correct url check
        if url.startswith('http'):
            source = io.BytesIO(requests.get(url).content)
            self._image = Img.open(source)
            print('Image loaded from - ', url)
        else:
            self._image = Img.open(url)

        self._all_colors = self._image.getcolors(maxcolors=MAX_COLORS)
        self._all_colors_len = len(self._all_colors)
        self._hash = self._generate_hash()
        self._url = url

    def get_params(self):
        """
        Returns image properties
        :return: dict of image_property|value
        """
        return {
            'width': self._image.size[0],
            'height': self._image.size[1],
            'format': self._image.format,
            'colors_count': self._all_colors_len,
            'mono': self._is_mono(),
            'hash': str(self._hash),
            'url': self._url
        }

    def _is_mono(self):
        """
        Checks if an image is an monochrome image.
        :return: True if image is monochrome
        """
        if self._all_colors_len > 2:
            return False

        rgbs = [rgba[:3] for _, rgba in self._all_colors]

        return all(rgb in ((0, 0, 0), (255, 255, 255)) for rgb in rgbs)

    def _generate_hash(self):
        """
        Generates phash for storing and filtering image.
        :return: Phash string
        """
        return imagehash.phash(self._image)

    @property
    def get_hash(self):
        """
        The public getter of hash
        :return: the image hash
        """
        return self._hash

    @property
    def url(self):
        return self._url
