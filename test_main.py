import unittest
import requests
from app import app

class FlaskTestCase(unittest.TestCase):

    def create_app(self):
            return app
        
    def test_classify(self):
        input_data = {"pixels": [0 for i in range(784)]}
        
        print('1')
        response = requests.post("http://localhost:5000/classify", json=input_data)
        print('2')
        result = response.json()
        print('3')
        expected_result = {"class": 0}
        print('4')
        assert result == expected_result, f"Expected {expected_result} but got {result}"
        
if __name__ == '__main__':
    unittest.main()
