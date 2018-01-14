import requests
from flask import Flask
from flask_testing import LiveServerTestCase


# Testing with LiveServer
class MyTest(LiveServerTestCase):
    # if the create_app is not implemented NotImplementedError will be raised
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5001
        return app

    def test_flask_application_is_up_and_running(self):
        # app = self.create_app()
        # app.run()
        print(self.get_server_url())
        with requests.get(self.get_server_url()) as response:
            print(response.status_code)
            # self.assertEqual(response.code, 404)

