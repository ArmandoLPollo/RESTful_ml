import unittest
import requests
from app import app

class FlaskTestCase(unittest.TestCase):
    

    def create_app(self):
        return app
    
    def test_classify(self):
        # Define the API endpoint URL
        url = "http://localhost:5000/classify"
        print('1')
        # Define the data to send in the request using list comprehension
        data = {
            "pixels": [0.0 for i in range(784)]
        }
        print('2')
        # Send a POST request to the API endpoint
        response = requests.post(url, json=data)
        print('3')
        # Get the response data
        response_data = json.loads(response.text)
        print('4')
        # Define the expected result
        expected_result = {"class": "T-shirt"}
        print('5')
        # Compare the result of the API with the expected value
        self.assertEqual(response_data, expected_result)
        
if __name__ == '__main__':
    unittest.main()
