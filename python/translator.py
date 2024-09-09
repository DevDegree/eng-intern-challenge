import sys
from data import dictionary, dictionary_number


def translator(text):

    # determine the language, if the text consists of only . and 0, then it is braille
    if set(text) == {'.', 'O'}:
        return from_b_to_e(text)
    else:
        return from_e_to_b(text)


def from_b_to_e(text):
    # split string into groups of 6 characters
    text_array = [text[i:i+6] for i in range(0, len(text), 6)]
    translated_array = []

    number_mode = False

    # loop through each item in text_array
    for i in range(len(text_array)):

        if dictionary[text_array[i]] == 'number follows':
            number_mode = True
            continue

        if dictionary[text_array[i]] == ' ':
            number_mode = False
            translated_array.append(' ')
            continue

        if number_mode is True:
            if dictionary_number[text_array[i]] is not None:
                translated_array.append(dictionary_number[text_array[i]])

        if i > 0 and dictionary[text_array[i-1]] == 'capital follows':
            translated_array.append(text_array[i])
            continue

        if dictionary[text_array[i]] == 'capital follows':
            continue

        else:
            translated_array.append(text_array[i].lower())

    return ''.join(translated_array)


def from_e_to_b(text):

    translated_array = []

    for char in text:
        char = str(char)
        if char.isupper():
            translated_array.append(dictionary['capital follows'])
            translated_array.append(dictionary[char.lower()])
        elif char.isdigit():
            translated_array.append(dictionary['number follows'])
            translated_array.append(dictionary[char])
        else:
            translated_array.append(dictionary[char])

    return ''.join(translated_array)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translator.py text")
        sys.exit(1)

    text = ' '.join(sys.argv[1:])

    translated_text = translator(text)
    print(translated_text)


if __name__ == "__main__":
    main()
