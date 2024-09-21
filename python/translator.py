import sys

English_dict = {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    "capital": ".....O",
    "decimal": ".O...O",
    "number": ".O.OOO",
}

Braille_dict = {
    "O.....": "a",
    "O.O...": "b",
    "OO....": "c",
    "OO.O..": "d",
    "O..O..": "e",
    "OOO...": "f",
    "OOOO..": "g",
    "O.OO..": "h",
    ".OO...": "i",
    ".OOO..": "j",
    "O...O.": "k",
    "O.O.O.": "l",
    "OO..O.": "m",
    "OO.OO.": "n",
    "O..OO.": "o",
    "OOO.O.": "p",
    "OOOOO.": "q",
    "O.OOO.": "r",
    ".OO.O.": "s",
    ".OOOO.": "t",
    "O...OO": "u",
    "O.O.OO": "v",
    ".OOO.O": "w",
    "OO..OO": "x",
    "OO.OOO": "y",
    "O..OOO": "z",
    ".....O": "capital",
    "......": "space",
    ".O.OOO": "number",
}



def is_content_English(content):
    if '.' in content[1]:
        return False
    else:
        return True


def translate_to_Braille(English):
    i = 0
    ans = ""
    content_len = len(English) - 1
    for word in English:
        is_number = False
        if i == 0:
            i += 1
            continue
        else:
            i += 1
            for letter in word:
                if ord(letter) >= ord('0') and ord(letter) <= ord('9') and not is_number:
                    is_number = True
                    ans += English_dict["number"]
                if not is_number:
                    if letter.isupper():
                        ans += English_dict['capital']
                    ans += English_dict[letter.lower()]
                elif letter == '0':
                    ans += English_dict['j']
                else:
                    ans += English_dict[chr(ord('a') + ord(letter) - ord('1'))]
            if i < content_len + 1:
                ans += "......"
    return ans


def translate_to_English(Braille):
    ans = ""
    is_number = False
    is_capital = False
    word_len = int(len(Braille) / 6)
    for i in range(word_len):
        left = i * 6
        right = (i + 1) * 6
        word = Braille[left: right]
        english_word = Braille_dict[word]
        if english_word == "number":
            is_number = True
        elif english_word == "capital":
            is_capital = True
        elif english_word == "space":
            is_number = False
            ans += " "
        elif is_number == True and english_word != 'j':
            ans += chr(ord('1') + ord(english_word) - ord('a'))
        elif is_number == True and english_word == 'j':
            ans += "0"
        elif is_capital == True:
            ans += english_word.upper()
            is_capital = False
        else:
            ans += english_word
    return ans


def translate(content):
    is_English = is_content_English(content)
    ans = ""
    if not is_English:
        ans = translate_to_English(content[1])
    else:
        ans = translate_to_Braille(content)
    print(ans)


if __name__ == '__main__':
    translate(sys.argv)
