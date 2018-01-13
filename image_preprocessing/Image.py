from skimage import io, color


class Image:
    def __init__(self, url):
        self._image = io.imread(url)
        print(self._image)
        dimensions = color.guess_spatial_dimensions(self._image)
        print(dimensions)

    def get_image(self):
        return self._image


if __name__ == '__main__':
    image = Image('images/test.jpg')
