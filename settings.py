# DATABASE

DB = 'test'
COLLECTION = 'image'
HOST = 'localhost'
PORT = 27017

# CELERY

BROKER = 'pyamqp://guest@localhost//'
BACKEND = 'mongodb://{}:{}/test_celery'.format(HOST, PORT)
