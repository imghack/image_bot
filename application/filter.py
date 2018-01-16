# Creators: Vasiurin I., Taraman V.

from PIL import Image
import imagehash
from .workWithDB import WorkWithDB


class Filter:
    """
    Class for filtering duplicates images before pushing them into the db storage
    """
    @staticmethod
    def check_duplicate_by_hash(db_provider, hash_from_db):
        """
        The core entry point for checking duplicate image.
        This method is static and check images by hash
        :param db_provider: db connection provider
        :param hash_from_db: phash value of image
        :return: boolean value - is duplicate or not
        """
        if isinstance(db_provider, WorkWithDB):
            # if the returned tuple will be empty ({}), then it will be False (No duplicates)
            True if db_provider.get_image_by_hash(hash_from_db) else False


