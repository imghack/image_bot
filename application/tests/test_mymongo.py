import unittest

from PIL import Image
from application.tests.mocks.mock_mymongo import get_image_by_hash, get_all_images_count, save
import imagehash


class MyMongoTests(unittest.TestCase):

    def test_duplicate_from_db_pos(self):
        """Test for has duplicate scenario, when we get hash from db"""
        img_hash = imagehash.phash(Image.open('static/images/test42.jpg'))
        self.assertEqual(get_image_by_hash(img_hash), False)

    def test_duplicate_from_db_neg(self):
        """Test for has no duplicate scenario, when we get hash from db"""
        img_hash = imagehash.phash(Image.open('static/images/mono.png'))

        self.assertEqual(get_image_by_hash(img_hash), True)

    def test_all_images_count(self):
        """Test for counting images in db"""
        self.assertEqual(get_all_images_count(), 4)
        self.assertNotEqual(get_all_images_count(), 5)

# Test were commented, because are not used in the moment

# def test_duplicate_pos(self):
#     """
#     Test for has duplicate scenario, where input data are images
#     """
#     img_jpg = Image.open('static/images/test.jpg')
#     img_png = Image.open('static/images/test.png')
#     # must be duplicates
#     self.assertEqual(Filter.check_duplicate_img(img_jpg, img_png), True)
#
# def test_duplicate_neg(self):
#     """
#     Test for has no duplicate scenario, where input data are images
#     """
#     img1 = Image.open('static/images/test.jpg')
#     img2 = Image.open('static/images/test42.jpg')
#     self.assertEqual(Filter.check_duplicate_img(img1, img2), False)


if __name__ == "__main__":
    unittest.main()