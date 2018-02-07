import pymongo
from application import settings
import xml.etree.cElementTree as ET

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
    if not _get_image_by_hash(str(data['hash'])):
        cursor.insert_one(data)
        return True
    else:
        return False


def get_all_images():
    """
    :return: all data from db, except db id's
    """
    return list(cursor.find({}, {'_id': False}))


def get_all_images_count():
    return cursor.count()


def export_to_xml():
    """ Export to all images to xml as string
    :return: xml as string
    """
    root = ET.Element("root")
    images = ET.SubElement(root, "images")

    all_images = cursor.find({})
    for document in all_images:
        sub_element = ET.SubElement(images, "image")
        sub_element.text = document['url']
        for key in document:
            sub_element.set(key, str(document[key]))

    return ET.tostring(root, encoding='utf8', method='xml')


def _get_image_by_hash(hash_string):
    """Private Method used to get image tuple by hash
    :param hash_string: the p-hash string
    :return: the image tuples, that match hash-value
    """
    col = cursor.find({'hash': hash_string})
    return col[0] if col.count() > 0 else {}  # if there are values in db return the first one else empty({})
