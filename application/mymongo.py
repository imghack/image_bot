import pymongo
import settings

connection = pymongo.MongoClient(settings.HOST, settings.PORT)
db = connection[settings.DB]
cursor = db[settings.COLLECTION]


def save(data):
    """Db-saver method
    :param data: data to save in mongoDB
    :return: boolean that represents if data was inserted or not
    """
    # the check duplicate method was moved to DB-class
    # because it is more suitable to check data here
    if not get_image_by_hash(str(data['hash'])):
        cursor.insert_one(data)
        return True
    else:
        return False


def get_all_images_count():
    return cursor.count()


def get_image_by_hash(hash_string):
    """Method used to get image tuple by hash
    :param hash_string: the p-hash string
    :return: the image tuples, that match hash-value
    """
    col = cursor.find({'hash': hash_string})
    return col[0] if col.count() > 0 else {}  # if there are values in db return the first one else empty({})

