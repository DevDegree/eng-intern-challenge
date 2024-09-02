import argparse

# Binary representation of A-Z
braille_dict = {
    32: 'a',
    40: 'b',
    48: 'c',
    52: 'd',
    36: 'e',
    56: 'f',
    60: 'g',
    44: 'h',
    24: 'i',
    28: 'j',
    34: 'k',
    42: 'l',
    50: 'm',
    54: 'n',
    38: 'o',
    58: 'p',
    62: 'q',
    46: 'r',
    26: 's',
    30: 't',
    35: 'u',
    43: 'v',
    29: 'w',
    51: 'x',
    55: 'y',
    39: 'z',
    1: "CAPITAL_FOLLOWS",
    17: "DECIMAL_FOLLOWS",
    23: "NUMBER_FOLLOWS",
    13: ".",
    8: ",",
    11: "?",
    14: "!",
    12: ":",
    10: ";",
    3: "-",
    18: "/",
    25: "<",
    # 38: ">", # WARNING CLASH
    41: "(",
    22: ")",
    0: "SPACE"
}

number_dict = {
    32: '1',
    40: '2',
    48: '3',
    52: '4',
    36: '5',
    56: '6',
    60: '7',
    44: '8',
    24: '9',
    28: '0',
}

reverse_braille_dict = {v: k for k, v in braille_dict.items()}
reverse_number_dict = {v: k for k, v in number_dict.items()}

UNKNOWN_PLACEHOLDER = "█"
NUM_DOTS_PER_TOKEN = 6

def to_braille(char):
    binary_representation = bin(int(char))[2:]
    padded_binary_representation = '0' * (NUM_DOTS_PER_TOKEN - len(binary_representation)) + binary_representation
    return padded_binary_representation.replace('0', '.').replace('1', 'O')

def is_braille(payload):
    for char in payload:
        if char not in ['.', 'O']:
            return False
    return True

def braille_to_char(token, capital_follows=False, number_follows=False):
    token = token.replace('.', '0').replace('O', '1')

    if number_follows:
        return number_dict.get(int(token, 2), UNKNOWN_PLACEHOLDER)

    if capital_follows:
        return braille_dict.get(int(token, 2), UNKNOWN_PLACEHOLDER).upper()
    
    return braille_dict.get(int(token, 2), UNKNOWN_PLACEHOLDER)


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="CMD-line Braille Translator")

    # Add arguments
    parser.add_argument('args', nargs='*', help='Payload to be parsed by the translator')

    # Parse the arguments
    args = parser.parse_args()

    # Process the arguments ---------------------------------------------
    
    payload_is_braille = len(args.args) == 1 and is_braille(''.join(args.args)) # Optimization: terminate early if more than one continuous string is passed
    output = ""

    capital_follows_toggle = False # only the next
    number_follows_toggle = False # until the next space

    if payload_is_braille:
        payload = args.args[0]
        num_tokens = len(payload) // NUM_DOTS_PER_TOKEN

        for i in range(num_tokens):
            start = i * NUM_DOTS_PER_TOKEN
            end = start + NUM_DOTS_PER_TOKEN # exclusive
            token = payload[start:end]
            
            translated = braille_to_char(token)

            if translated == "CAPITAL_FOLLOWS":
                capital_follows_toggle = True
                continue

            if translated == "NUMBER_FOLLOWS":
                number_follows_toggle = True
                continue

            if translated == "SPACE":
                output += " "
                number_follows_toggle = False
                continue
            
            output += braille_to_char(token, capital_follows_toggle, number_follows_toggle)

            if capital_follows_toggle:
                capital_follows_toggle = False

    else:
        payload = ' '.join(args.args)

        for char in payload:
            if char == ' ':
                output += to_braille(reverse_braille_dict.get("SPACE", UNKNOWN_PLACEHOLDER))
                number_follows_toggle = False
                continue

            if char.isdigit() and not number_follows_toggle:
                number_follows_toggle = True
                output += to_braille(reverse_braille_dict.get("NUMBER_FOLLOWS", UNKNOWN_PLACEHOLDER))
                output += to_braille(reverse_number_dict.get(char, UNKNOWN_PLACEHOLDER))
                continue

            if char.isupper():
                output += to_braille(reverse_braille_dict.get("CAPITAL_FOLLOWS", UNKNOWN_PLACEHOLDER))
                char = char.lower()

            output += to_braille(reverse_braille_dict.get(char, UNKNOWN_PLACEHOLDER))
    
    print(output)

if __name__ == "__main__":
    main()
