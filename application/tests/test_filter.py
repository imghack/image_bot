import unittest

from application.filter import Filter
from PIL import Image
from application.tests.mocks.mock_db_helper import MockWorkWithDB
import imagehash


class FilterTests(unittest.TestCase):

    def test_duplicate_pos(self):
        """
        Test for has duplicate scenario, where input data are images
        """
        img_jpg = Image.open('static/images/test.jpg')
        img_png = Image.open('static/images/test.png')
        # must be duplicates
        self.assertEqual(Filter.check_duplicate_img(img_jpg, img_png), True)

    def test_duplicate_neg(self):
        """
        Test for has no duplicate scenario, where input data are images
        """
        img1 = Image.open('static/images/test.jpg')
        img2 = Image.open('static/images/test42.jpg')
        self.assertEqual(Filter.check_duplicate_img(img1, img2), False)

    def test_duplicate_from_db_pos(self):
        """
        Test for has duplicate scenario, when we get hash from db
        """
        img_hash = imagehash.phash(Image.open('static/images/mono.png'))
        mock_db = MockWorkWithDB("fake", 0000)
        self.assertEqual(Filter.check_duplicate_in_db(mock_db, img_hash), True)

    def test_duplicate_from_db_neg(self):
        """
        Test for has no duplicate scenario, when we get hash from db
        """
        img_hash = imagehash.phash(Image.open('static/images/test.jpg'))
        mock_db = MockWorkWithDB("fake", 0000)
        self.assertEqual(Filter.check_duplicate_in_db(mock_db, img_hash), False)


if __name__ == "__main__":
    unittest.main()