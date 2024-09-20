import yaml, string

class Braille_Translator():

    def __init__(self):
        # Import braille from yaml file
        with open("braille.yml", 'r') as file:
            braille = yaml.safe_load(file)["braille"]

        # Extract Braille special chars
        self._capital_follows = braille["special_chars"]["capital_follows"]
        self._number_follows = braille["special_chars"]["number_follows"]
        self._space = braille["special_chars"][' ']

        # Define English-Braille alphabet and digit maps
        self._eng_to_braille_alphabet_map = { k: braille["alphabet"][k] for k in string.ascii_lowercase }
        self._eng_to_braille_digit_map = { k: braille["digits"][k] for k in string.digits }
        
        # Define Braille-English maps by flipping
        self._braille_to_eng_alphabet_map = { v: k for k, v in self._eng_to_braille_alphabet_map.items() }
        self._braille_to_eng_digit_map = { v: k for k, v in self._eng_to_braille_digit_map.items() }



    def is_braille(self, input: str) -> bool:
        pass


    def eng_to_braille(self, english: str) -> str:
        pass


    def braille_to_eng(self, braille: str) -> str:
        pass


    def translate(self, input: str) -> str:
        pass