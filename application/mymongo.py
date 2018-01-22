import pymongo
import settings

connection = pymongo.MongoClient(settings.HOST, settings.PORT)
db = connection[settings.DB]
cursor = db[settings.COLLECTION]


def save(data):
    cursor.insert_one(data)


def get_all_images_count():
    return cursor.count()


def get_image_by_hash(hash_string):
    """
    Method used to get image tuple by hash
    :param hash: the phash string
    :return: the image tuples, that match hash-value
    """
    col = cursor.find({'hash': hash_string})
    return col[0] if col.count() > 0 else {}  # if there are values in db return the first one else empty({})

