# Mock object that overrides working with db class
from PIL import Image
import imagehash

"""Mock functions for testing db functionality"""

def save(data):
    pass

def get_all_images_count():
    return 4

def get_image_by_hash(hash_string):
    if str(hash_string) == "820002000200a800":
        return bool({'width': 1200, 'height': 1200, 'format': 'PNG', 'colors_count': 2, 'mono': True,
                'hash': '820002000200a800'})
    else:
        return bool({})
