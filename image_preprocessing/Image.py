from PIL import Image as Img

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

        rgbs = [color[1][:3] for color in self._all_colors]

        for rgb in rgbs:
            if rgb != (0, 0, 0) and rgb != (255, 255, 255):
                return False
        return True


if __name__ == '__main__':
    image = Image('images/test.jpg')
    params = image.get_params()

    image_mono = Image('images/mono.png')
    params_mono = image_mono.get_params()

    print(params)
    print(params_mono)
