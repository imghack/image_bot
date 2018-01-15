import pymongo
import base64
from PIL import Image

class DBConnect:
    def db_connect(self, db, collection):
        connection = pymongo.MongoClient('localhost', 27017)
        db = connection[db]
        col = db[collection]
        return col


class ImageMongoSaver:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    def saver(self, path):
        with open(path, "rb") as image_file:
            image_str = base64.b64encode(image_file.read())

            conn = DBConnect()
            cursor = conn.db_connect(self.db, self.collection)

            image = Image.open(path)

            document_to_save = {'type' : 'image',
                                'format' : image.format,
                                'size' : image.size,
                                'image' : image_str
                                }

            cursor.insert_one(document_to_save)


image_to_save = ImageMongoSaver('test', 'image')
image_to_save.saver('1.png')