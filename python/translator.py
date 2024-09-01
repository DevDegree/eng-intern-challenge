import argparse

NUM_DOTS_PER_TOKEN = 6

def is_braille(payload):
    for char in payload:
        if char not in ['.', 'O']:
            return False
    return True

def translate_braille(token):
    if len(token) != NUM_DOTS_PER_TOKEN:
        raise ValueError("Invalid token length")
    
    token = token.replace('.', '0').replace('O', '1')
    
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

    return braille_dict.get(int(token, 2), "UNKNOWN")    

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

    if payload_is_braille:
        payload = args.args[0]
        num_tokens = len(payload) // NUM_DOTS_PER_TOKEN
        
        capital_follows_toggle = False # only the next
        number_follows_toggle = False # until the next space

        for i in range(num_tokens):
            start = i * NUM_DOTS_PER_TOKEN
            end = start + NUM_DOTS_PER_TOKEN # exclusive
            token = payload[start:end]
            translated = translate_braille(token)

            if capital_follows_toggle:
                output += translated.upper()
                capital_follows_toggle = False
                continue

            # number follows toggle

            if translated == "CAPITAL_FOLLOWS":
                capital_follows_toggle = True
                continue

            if translated == "NUMBER_FOLLOWS":
                number_follows_toggle = True
                continue

    else:
        print("Braille not detected")
    
    print(output)

if __name__ == "__main__":
    main()
