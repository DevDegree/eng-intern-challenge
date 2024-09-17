import sys

# The following are the positions of the dots in a 2x3 grid, adjusted for 0 indexing
dot_positions = {
    1: 0,  
    2: 1,  
    3: 2,  
    4: 3,  
    5: 4,  
    6: 5,  
}

# The mappings for letters to their Braille dots
letter_to_dots = {
    'a': [1],
    'b': [1,3],
    'c': [1,2],
    'd': [1,2,4],  
    'e': [1,4],
    'f': [1,2,3],
    'g': [1,2,3,4],
    'h': [1,3,4],
    'i': [2,3],
    'j': [2,3,4],
    'k': [1,5],
    'l': [1,3,5],
    'm': [1,2,5],
    'n': [1,2,4,5],
    'o': [1,4,5],
    'p': [1,2,3,5],
    'q': [1,2,3,4,5],
    'r': [1,3,4,5],
    's': [2,3,5],
    't': [2,3,4,5],
    'u': [1,5,6],
    'v': [1,3,5,6],
    'w': [2,3,4,6],
    'x': [1,2,5,6],
    'y': [1,2,4,5,6],
    'z': [1,4,5,6],
}

# Since the numbers are represented by the same dots as some of the letters, we can use the same mapping
number_to_letter = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    '7': 'g',
    '8': 'h',
    '9': 'i',
    '0': 'j',
}

capital_follows_dots = [6] 
number_follows_dots = [2,4,5,6] 

# The following actually maps the Braille to the letter in English
dots_to_letter = {}
for letter, dots in letter_to_dots.items():
    braille = ['.'] * 6
    for dot in dots:
        index = dot_positions[dot]
        braille[index] = 'O'
    braille_str = ''.join(braille)
    dots_to_letter[braille_str] = letter

# The following converts the dots to Braille
def dots_to_braille(dots):
    braille = ['.'] * 6
    for dot in dots:
        index = dot_positions[dot]
        braille[index] = 'O'
    return ''.join(braille)

capital_follows_braille = dots_to_braille(capital_follows_dots)
number_follows_braille = dots_to_braille(number_follows_dots)
dots_to_letter[capital_follows_braille] = 'capital'
dots_to_letter[number_follows_braille] = 'number'

# basic boolean check to see if the input is Braille or English
def is_braille(input_str):
    valid_chars = {'O', '.', ' '}
    return set(input_str).issubset(valid_chars)

def translate_to_braille(text):
    result = []
    for word in text.split(' '): #split the text into words
        number_mode = False
        for char in word:
            if char.isdigit(): #check if the character is a number and if it is not already in number mode (to avoid repeating the number pattern)
                if not number_mode:
                    result.append(number_follows_braille)
                    number_mode = True
                letter = number_to_letter[char]
                braille_char = dots_to_braille(letter_to_dots[letter])
                result.append(braille_char)
            else:
                number_mode = False
                if char.isupper(): #check if the character is uppercase and if it is not already in capital mode (to avoid repeating the capital pattern)
                    result.append(capital_follows_braille)
                    char = char.lower()
                if char.lower() in letter_to_dots:
                    braille_char = dots_to_braille(letter_to_dots[char.lower()])
                    result.append(braille_char)
        result.append('......')  #append the space between words
    if result and result[-1] == '......':
        result.pop()
    return ''.join(result).strip()

def translate_to_english(braille_text):
    result = []
    tokens = []
    temp = ''
    i = 0
    while i < len(braille_text): #iterate through the Braille text
        if braille_text[i:i+6] == '......' and temp == '': #check that temp string is empty so that we don't add extra spaces, i.e for letter 'o'
            tokens.append(' ')  
            i += 6
            temp = ''
            continue
        elif braille_text[i] in {'O', '.'}:
            temp += braille_text[i]
            i += 1
            if len(temp) == 6: #append the temp string to the tokens list and reset the temp string, (since we know that the length is 6)
                tokens.append(temp)
                temp = ''
    if temp:
        tokens.append(temp)
    index = 0
    capital_next = False
    number_mode = False
    while index < len(tokens): #iterate through the tokens list and convert the Braille to English
        token = tokens[index]
        if token == ' ':
            result.append(' ')
            capital_next = False
            number_mode = False
            index += 1
            continue
        if token not in dots_to_letter:
            index += 1
            continue
        symbol = dots_to_letter[token]
        if symbol == 'capital':
            capital_next = True
        elif symbol == 'number':
            number_mode = True
        else:
            if number_mode:
                for num, letter in number_to_letter.items():
                    if letter == symbol:
                        result.append(num)
                        break
            else:
                if capital_next:
                    result.append(symbol.upper())
                    capital_next = False
                else:
                    result.append(symbol)
        index += 1
    return ''.join(result)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    input_str = ' '.join(sys.argv[1:])
    if is_braille(input_str):
        english_text = translate_to_english(input_str)
        print(english_text)
    else:
        braille_text = translate_to_braille(input_str)
        print(braille_text)

if __name__ == "__main__":
    main()
