# Class for filtering duplicates images before pushing them into the db storage
# Creators: Vasiurin I., Taraman V.

from PIL import Image
import imagehash


class Filter:

    @staticmethod
    def check_duplicate(image_url, hash_from_DB):
        """
        The core entry point for checking duplicate image.
        This method is static and includes ways of finding duplicates
        :return: boolean value - is duplicate or not
        """
        target_hash = imagehash.average_hash(Image.open(image_url))
        return True if target_hash == hash_from_DB else False


