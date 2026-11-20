import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def test_home(self):
        client = app.test_client()
        response = client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, Jenkins!")

if __name__ == '__main__':
    unittest.main()