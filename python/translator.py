import sys
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_char = False
        self.char = None

class BrailleTrie:
    def __init__(self):
        self.root = TrieNode()
        self.capital_follows = ".....O"
        self.number_follows = ".O.OOO"
        self.braille_space = '......'
    
    def insert(self, braille_str, char):
        node = self.root
        for symbol in braille_str:
            if symbol not in node.children:
                node.children[symbol] = TrieNode()
            node = node.children[symbol]
        node.is_end_of_char = True
        node.char = char
    
    def search(self, braille_str):
        node = self.root
        for symbol in braille_str:
            if symbol in node.children:
                node = node.children[symbol]
            else:
                return None
        return node.char if node.is_end_of_char else None


# Initialize the Braille-to-English mapping using Trie
braille_trie = BrailleTrie()

# Insert mappings for Braille letters (a-z)
braille_to_english = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
}

# Insert all mappings into the Trie
for braille, char in braille_to_english.items():
    braille_trie.insert(braille, char)

# Insert digits 0-9 using braille letters a-j for numbers
for i, num in enumerate("0123456789"):
    braille_trie.insert(braille_to_english[chr(ord('a') + i)], num)

# Reverse dictionary for English-to-Braille
english_to_braille = {v: k for k, v in braille_to_english.items()}

# Function to handle Braille to English translation using the optimized Trie approach
def translate_braille_to_english_trie(braille_input):
    output = []
    i = 0
    is_capital = False
    is_number = False

    # Pre-process the input into chunks of 6 characters
    braille_chunks = [braille_input[i:i+6] for i in range(0, len(braille_input), 6)]

    for braille_char in braille_chunks:
        # Check for capital or number follow prefixes
        if braille_char == braille_trie.capital_follows:
            is_capital = True
            continue
        elif braille_char == braille_trie.number_follows:
            is_number = True
            continue
        elif braille_char == braille_trie.braille_space:
            output.append(' ')  # Handle space
            continue
        
        # Search for the corresponding English character in Trie
        char = braille_trie.search(braille_char)
        if char:
            if is_number:
                output.append(char)  # Numbers are treated as is
                is_number = False  # Reset number mode
            else:
                if is_capital:
                    output.append(char.upper())  # Capitalize the letter
                    is_capital = False  # Reset capital mode
                else:
                    output.append(char)

    return ''.join(output)

# Function to handle English to Braille translation
def translate_english_to_braille_trie(english_input):
    output = []
    for char in english_input:
        if char.isupper():
            output.append(braille_trie.capital_follows)
            char = char.lower()
        if char.isdigit():
            output.append(braille_trie.number_follows)
            output.append(english_to_braille[chr(ord('a') + int(char))])
        elif char in english_to_braille:
            output.append(english_to_braille[char])
        elif char == ' ':
            output.append(braille_trie.braille_space)  # Braille space
    return ''.join(output)

def is_braille(text):
    return all(char in '.O' for char in text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text_to_translate>")
        sys.exit(1)

    input_text = sys.argv[1]

    if is_braille(input_text):
        result = translate_braille_to_english_trie(input_text)
    else:
        result = translate_english_to_braille_trie(input_text)

    print(result)

if __name__ == "__main__":
    main()
