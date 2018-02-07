import unittest

from . import create_app


class MainTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # def test_form_post_request(self):
    #     response = self.app.post('/parse', data={'url': 'http://example.com'})
    #     self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
