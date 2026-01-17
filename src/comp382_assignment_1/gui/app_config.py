import json
import os

class AppConfig:
    def __init__(self):
        # Loading strings
        json_path = os.path.join(os.path.dirname(__file__), 'strings.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Set attributes from JSON data
        for key, value in data.items():
            setattr(self, key, value)

        # Convert validation strings to sets for efficient lookup
        self.valid_regex_chars = set(self.valid_regex_chars)
        self.valid_test_string_chars = set(self.valid_test_string_chars)