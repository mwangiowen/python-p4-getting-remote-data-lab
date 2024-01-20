import requests
import json


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return (
            response.content
        )  # Use response.content to get the response body in bytes

    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = json.loads(
                response_body.decode("utf-8")
            )  # Decode bytes to UTF-8 before loading JSON
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error loading JSON: {e}")
            return None
