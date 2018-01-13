from PIL import Image as Img

MAX_COLORS = 1000000

class Image:
    def __init__(self, url):
        self._image = Img.open(url)

    def get_source(self):
        return self._image

    def get_params(self):
        all_colors = self._image.getcolors(maxcolors=MAX_COLORS)

        return {
            'width': self._image.size[0],
            'height': self._image.size[1],
            'format': self._image.format,
            'colors_count': len(all_colors),
            'mono': self._is_mono(all_colors)
        }

    def _is_mono(self, all_colors):
        if (len(all_colors) > 2):
            return False

        colors_rbg = [color[1][:3] for color in all_colors]

        for rgb in colors_rbg:
            if rgb == (0, 0, 0) or rgb == (255, 255, 255):
                return True
        return False


if __name__ == '__main__':
    image = Image('images/test.jpg')
    source = image.get_source()
    params = image.get_params()

    image_mono = Image('images/mono.png')
    source_mono = image_mono.get_source()
    params_mono = image_mono.get_params()

    print(params)
    print(params_mono)
