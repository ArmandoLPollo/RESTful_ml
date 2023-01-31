import unittest
import requests
from app import app

class FlaskTestCase(unittest.TestCase):

    def create_app(self):
            return app
        
if __name__ == '__main__':
    unittest.main()
