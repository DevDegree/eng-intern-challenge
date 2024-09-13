import sys

class Bidict(dict):
    # Bidirectional hash table makes it possible to use both key and value as input and retrieve the corresponding value/key,
    # while keeping the time complexity O(1). This makes the overall time complexity of the translation process for a string of length n to be O(n)
    def __init__(self, *args, **kwargs):
        super(Bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse[value] = key

    def __setitem__(self, key, value):
        super(Bidict, self).__setitem__(key, value)
        self.inverse[value] = key

class Translator():
    # The translator class
    # The main idea involves creating bidirectional hash tables of symbols and process the text to perform the translation.
    def __init__(self, sentence):
        self.sentence = sentence

        self.isBrailleToEnglish = None

        self.BRAILLE_TO_ENGLISH_ALPHABET = Bidict({
            'O.....': 'a',
            'O.O...': 'b',
            'OO....': 'c',
            'OO.O..': 'd',
            'O..O..': 'e',
            'OOO...': 'f',
            'OOOO..': 'g',
            'O.OO..': 'h',
            '.OO...': 'i',
            '.OOO..': 'j',
            'O...O.': 'k',
            'O.O.O.': 'l',
            'OO..O.': 'm',
            'OO.OO.': 'n',
            'O..OO.': 'o',
            'OOO.O.': 'p',
            'OOOOO.': 'q',
            'O.OOO.': 'r',
            '.OO.O.': 's',
            '.OOOO.': 't',
            'O...OO': 'u',
            'O.O.OO': 'v',
            '.OOO.O': 'w',
            'OO..OO': 'x',
            'OO.OOO': 'y',
            'O..OOO': 'z'
        })

        self.BRAILLE_TO_ENGLISH_NUMBERS = Bidict({
            'O.....': '1',
            'O.O...': '2',
            'OO....': '3',
            'OO.O..': '4',
            'O..O..': '5',
            'OOO...': '6',
            'OOOO..': '7',
            'O.OO..': '8',
            '.OO...': '9',
            '.OOO..': '0'
        })

        self.BRAILLE_TO_ENGLISH_SPECIAL = Bidict({
            '.....O': 'C',
            '.O...O': 'D',
            '.O.OOO': 'N'
        })

        self.BRAILLE_TO_ENGLISH_SYMBOLS = Bidict({
            '..OO.O': '.',
            '..O...': ',',
            '..O.OO': '?',
            '..OOO.': '!',
            '..OO..': ':',
            '..O.O.': ';',
            '....OO': '-',
            '.O..O.': '/',
            '.OO..O': '<',
            'O..OO.': '>',
            'O.O..O': '(',
            '.O.OO.': ')',
            '......': ' '
        })

    def setIsBrailleToEnglish(self):
        self.isBrailleToEnglish = True

        sentence_braille = [self.sentence[i:i+6] for i in range(0, len(self.sentence), 6)]
        for i in sentence_braille:
            if i not in self.BRAILLE_TO_ENGLISH_ALPHABET and i not in self.BRAILLE_TO_ENGLISH_NUMBERS and i not in self.BRAILLE_TO_ENGLISH_SPECIAL and i not in self.BRAILLE_TO_ENGLISH_SYMBOLS:
                self.isBrailleToEnglish = False
        
        if self.isBrailleToEnglish is False:
            sentence_english = self.sentence.lower()
            for i in list(sentence_english):
                if i not in self.BRAILLE_TO_ENGLISH_ALPHABET.inverse and i not in self.BRAILLE_TO_ENGLISH_NUMBERS.inverse and i not in self.BRAILLE_TO_ENGLISH_SYMBOLS.inverse:
                    raise KeyError(f'Invalid character passed in the input: {i}')
    
    def translate(self):
        self.setIsBrailleToEnglish()

        result = ''

        processed_sentence = None

        if self.isBrailleToEnglish:
            processed_sentence = [self.sentence[i:i+6] for i in range(0, len(self.sentence), 6)]
            isCapital = False
            isDecimal = False
            isNumber = False

            for i in processed_sentence:
                if i in self.BRAILLE_TO_ENGLISH_SPECIAL:
                    value = self.BRAILLE_TO_ENGLISH_SPECIAL[i]
                    if value == 'C':
                        isCapital = True
                    elif value == 'D': 
                        # I did not understand the use of this symbol. In the WikiPedia is says this symbol is decimal point but based on the instructions, when a 'number follows' symbol is used,
                        # I should assume all following symbols are numbers until the next space symbol. So it's impossible to have something like '2.5' in the input.
                        # I tried to cover both senarios.
                        isDecimal = True
                        result += '.'
                    else:
                        isNumber = True
                elif isNumber:
                    if i in self.BRAILLE_TO_ENGLISH_NUMBERS:
                        result += self.BRAILLE_TO_ENGLISH_NUMBERS[i]
                    elif i in self.BRAILLE_TO_ENGLISH_SYMBOLS:
                        if self.BRAILLE_TO_ENGLISH_SYMBOLS[i] == ' ':
                            isNumber = False
                            result += ' '
                    else:
                        raise ValueError(f'Expected number but found: {i}')
                elif isCapital:
                    if i in self.BRAILLE_TO_ENGLISH_ALPHABET:
                        result += self.BRAILLE_TO_ENGLISH_ALPHABET[i].upper()
                        isCapital = False
                    else:
                        raise ValueError(f'Expected alphabetical character but found: {i}')
                else:
                    if i in self.BRAILLE_TO_ENGLISH_ALPHABET:
                        result += self.BRAILLE_TO_ENGLISH_ALPHABET[i]
                    elif i in self.BRAILLE_TO_ENGLISH_SYMBOLS:
                        result += self.BRAILLE_TO_ENGLISH_SYMBOLS[i]
                    elif i in self.BRAILLE_TO_ENGLISH_NUMBERS:
                        raise ValueError(f'Number found without number indicator: {i}')

        else:
            processed_sentence = list(self.sentence)
            for index, i in enumerate(processed_sentence):
                if i.isalpha():
                    if index != 0 and processed_sentence[index - 1].isnumeric():
                        raise ValueError(f'Character cannot appear directly after number: {i}')
                    if i.isupper():
                        result += self.BRAILLE_TO_ENGLISH_SPECIAL.inverse['C']
                        result += self.BRAILLE_TO_ENGLISH_ALPHABET.inverse[i.lower()]
                    else:
                        result += self.BRAILLE_TO_ENGLISH_ALPHABET.inverse[i]
                elif i.isnumeric():
                    if (index == 0 or not processed_sentence[index - 1].isnumeric()) and processed_sentence[index - 1] != '.':
                        result += self.BRAILLE_TO_ENGLISH_SPECIAL.inverse['N']
                    result += self.BRAILLE_TO_ENGLISH_NUMBERS.inverse[i]
                elif i == '.':
                    if index != 0 and processed_sentence[index - 1].isnumeric() and index + 1 < len(processed_sentence) and processed_sentence[index + 1].isnumeric():
                        result += self.BRAILLE_TO_ENGLISH_SPECIAL.inverse['D']
                    else:
                        result += self.BRAILLE_TO_ENGLISH_SYMBOLS.inverse[i]
                elif i in self.BRAILLE_TO_ENGLISH_SYMBOLS.inverse:
                    result += self.BRAILLE_TO_ENGLISH_SYMBOLS.inverse[i]
                else:
                    raise ValueError(f'Invalid character found: {i}')

        return result


if __name__ == '__main__':
    sentence = ' '.join(sys.argv[1:])
    translator = Translator(sentence)
    result = translator.translate()
    print(result)
