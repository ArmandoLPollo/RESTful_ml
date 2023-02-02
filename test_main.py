import unittest
import requests
from app import app

class FlaskTestCase(unittest.TestCase):
    

    def create_app(self):
        return app
    
    def test_classify(self):
        # Define the API endpoint URL
        url = "http://localhost:5000/classify"
        # Define the data to send in the request using list comprehension
        data = {
            "pixels": [0.0 for i in range(784)]
        }
        print(data)
        # Send a POST request to the API endpoint
        response = requests.post(url, json=data)
        # Get the response data
        response_data = response.json()
        # Define the expected result
        expected_result = {"class": "0"}
        # Compare the result of the API with the expected value
        assert result == expected_result, f"Expected {expected_result} but got the following repsonse {response_data}"
        
if __name__ == '__main__':
    unittest.main()
