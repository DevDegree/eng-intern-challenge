import json
from utils.bidirectional_map import BidirectionalMap

class LanguageDictionary:
    def __init__(self, json_file):
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                self.letters = BidirectionalMap(data.get('letters'))
                self.numbers = BidirectionalMap(data.get('numbers'))
                self.special_chars = BidirectionalMap(data.get('special_chars'))

        except FileNotFoundError:
            raise FileNotFoundError(f"File {json_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON file {json_file}")
        except Exception as e:
            raise Exception(f"Unexpected Error occurred: {str(e)}")


    def get_letter(self, char, isKey=True):
        if isKey:
            return self.letters.get_key(char)
        else:
            return self.letters.get_value(char)
        self.letters = 