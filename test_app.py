import unittest
from main import app  # Assuming the given code is saved in a file named 'app.py'
import json

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_call_llama2_server(self):
        # Given
        payload = {
            "question": "What is the capital of France?"
        }
        headers = {
            'Content-Type': 'application/json'
        }

        # When
        response = self.app.post('/call_llama2', data=json.dumps(payload), headers=headers)
        print(">>",response)
        # Then
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, "What is the capital of France?")

if __name__ == '__main__':
    unittest.main()
