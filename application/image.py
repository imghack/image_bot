from PIL import Image as Img
import imagehash

# Limit of max image colors
# TODO : change to 2 ** 48 fix OverflowError: signed integer is greater than maximum
MAX_COLORS = 2 ** 24


class Image:
    def __init__(self, url):
        self._image = Img.open(url)
        self._all_colors = self._image.getcolors(maxcolors=MAX_COLORS)
        self._all_colors_len = len(self._all_colors)

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
            'mono': self._is_mono()
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

    def generate_hash(self):
        """
        Generates phash for storing and filtering image.
        :return: Phash string
        """
        return imagehash.average_hash(self._image)

