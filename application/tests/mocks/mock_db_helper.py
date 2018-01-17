# Mock object that overrides working with db class
from application.workWithDB import WorkWithDB
from PIL import Image
import imagehash


class MockWorkWithDB(WorkWithDB):
    """
    Mock class for testing db functionality
    """
    def save(self, data):
        ...

    def get_all_images_count(self):
        return 4

    def get_image_by_hash(self, hash_string):
        if hash_string == "820002000200a800":
            return {'width': 1200, 'height': 1200, 'format': 'PNG', 'colors_count': 2, 'mono': True,
                    'hash': '820002000200a800'}
        else:
            return {}
