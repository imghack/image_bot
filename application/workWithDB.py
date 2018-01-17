import pymongo
import base64
from .image import Image
import settings
from hashlib import md5


class DBConnect:
    @classmethod
    def db_connect(self, db, collection):
        connection = pymongo.MongoClient(settings.HOST, settings.PORT)
        db = connection[db]
        col = db[collection]
        return col


class WorkWithDB:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def saver(self, url):
        """
        This method saves images' hash and params in DB
        :param url:
        :return:
        """
        with open(url, "rb") as image_file:
            image_str = base64.b64encode(image_file.read())
            hash = md5()
            hash.update(image_str)
            image_hash = hash.hexdigest()
            #conn = DBConnect()
            cursor = DBConnect().db_connect(self.db, self.collection)
            image = Image(url)
            document_to_save = {'type' : 'image', 'image_hash' : image_hash, }
            document_to_save.update(image.get_params())
            cursor.insert_one(document_to_save)

    def save(self, data):
        conn = DBConnect()
        cursor = conn.db_connect(self.db, self.collection)
        cursor.insert_one(data)

    def get_all_images_count(self):
        """
        This method returns all documents number
        :return:
        """
        cursor = DBConnect().db_connect(self.db, self.collection)
        return cursor.count()

    def get_image_by_hash(self, hash_string):
        """
        Method used to get image tuple by hash
        :param hash: the phash string
        :return: the image tuples, that match hash-value
        """
        cursor = DBConnect().db_connect(self.db, self.collection)
        col = cursor.find({'hash': hash_string})
        return col[0] if col.count() > 0 else {}  # if there are values in db return the first one else empty({})

    # def duplicates_check(self, url):
    #     """
    #     This method checks is there image duplicate in DB by its hash
    #     :param url:
    #     :return:
    #     """
    #     with open(url, "rb") as image_file:
    #         image_str = base64.b64encode(image_file.read())
    #         hash = md5()
    #         hash.update(image_str)
    #         image_hash = hash.hexdigest()
    #         cursor = DBConnect().db_connect(self.db, self.collection)
    #         counter = cursor.count({'image_hash' : image_hash})
    #         if counter:
    #             print('The image is already in DB')
    #         else:
    #             print('This is new image')