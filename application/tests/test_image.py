import unittest

from application.image import Image


class ImageTests(unittest.TestCase):

    def test_image_is_mono(self):
        # TODO : use mock images
        image = Image('static/images/mono.png')
        self.assertEqual(image.get_params()['mono'], True)

    def test_image_is_not_mono(self):
        # TODO : use mock images
        image = Image('static/images/test.jpg')
        self.assertEqual(image.get_params()['mono'], False)


if __name__ == "__main__":
    unittest.main()
