import pymongo
from settings import HOST, PORT


class WorkWithDB:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def db_connect(self, db, collection):
        connection = pymongo.MongoClient(HOST, PORT)
        db = connection[db]
        col = db[collection]
        return col

    def save(self, data):
        cursor = self.db_connect(self.db, self.collection)
        cursor.insert_one(data)

    def get_all_images_count(self):
        """
        This method returns all documents number
        """
        cursor = self.db_connect(self.db, self.collection)
        return cursor.count()

    def get_image_by_hash(self, hash_string):
        """
        Method used to get image tuple by hash
        :param hash: the phash string
        :return: the image tuples, that match hash-value
        """
        cursor = self.db_connect(self.db, self.collection)
        col = cursor.find({'hash': hash_string})
        return col[0] if col.count() > 0 else {}  # if there are values in db return the first one else empty({})
