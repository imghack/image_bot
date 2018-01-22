# Creators: Vasiurin I., Taraman V.

from PIL import Image
import imagehash


class Filter:
    """
    Class for filtering duplicates images before pushing them into the db storage
    """
    @staticmethod
    def check_duplicate_in_db(db_provider, hash_from_db):
        """
        The core entry point for checking duplicate image.
        This method is static and check images by hash with db
        :param db_provider: db connection provider
        :param hash_from_db: phash value of image
        :return: boolean value - is duplicate or not
        """
        # if the returned tuple will be empty ({}), then it will be False (No duplicates)
        return True if db_provider.get_image_by_hash(str(hash_from_db)) else False

    @staticmethod
    def check_duplicate_img(img_in, img_out):
        """
        The method that was created to compare images using hash-transforming
        :param img_in: hash of the inserting img
        :param img_out: hash of the output img
        :return: boolean value - is duplicate or not
        """
        hash_img_in = imagehash.phash(img_in)
        hash_img_out = imagehash.phash(img_out)
        return hash_img_in == hash_img_out


