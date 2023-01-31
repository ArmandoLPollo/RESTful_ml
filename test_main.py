import unittest
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

        # Send a POST request to the API endpoint
        response = requests.post(url, json=data)

        # Get the response data
        response_data = json.loads(response.text)

        # Define the expected result
        expected_result = {"class": "T-shirt"}

        # Compare the result of the API with the expected value
        self.assertEqual(response_data, expected_result)

if __name__ == '__main__':
    unittest.main()
