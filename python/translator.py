import sys
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import List, Dict


class Language(Enum):
    """
    Enum of all possible language types
    """
    # English code
    ENGLISH = "en",
    # Braille code
    BRAILLE = "be"


class BaseTokenizer(metaclass=ABCMeta):
    """
    Abstract Tokenizer class.

    If adding new language support in the future, its corresponding tokenizer should be a subclass of BaseTokenizer.
    """

    @abstractmethod
    def tokenize(self, sentence: str) -> List[str]:
        """
        Tokenize the sentence into a list of tokens (translational units)
        :param sentence: string of sentence
        :return: a list of tokens
        """
        raise NotImplementedError


class BETokenizer(BaseTokenizer):
    """
    Tokenizer for breaking Braille language string into translational unit.
    """

    def tokenize(self, sentence: str) -> List[str]:
        """
        Split Braille language string into chunks of 6 characters.
        """
        if len(sentence) % 6 != 0:
            raise ValueError("Length of Braille sentence must be a multiple of 6 characters.")
        return [sentence[i:i + 6] for i in range(0, len(sentence), 6)]


class ENTokenizer(BaseTokenizer):
    """
    Tokenizer for breaking English language string into translational unit.
    """

    def tokenize(self, sentence: str) -> List[str]:
        """
        Split English language string into a list of letters
        :param sentence: English sentence
        :return: a list of letters
        """
        return list(sentence)


class BaseTranslator(metaclass=ABCMeta):
    """
    Abstract base class for all translators.
    NOTE: All translators must extend this class.
    """

    def __init__(self, tokenizer: BaseTokenizer):
        """
        Initialize translator with a given tokenizer
        :param tokenizer: tokenizer
        """
        self.tokenizer = tokenizer

    @abstractmethod
    def translate(self, sentence: str) -> str:
        """
        Translate a sentence using this translator
        :param sentence: a sentence in any language
        :return: translation result
        """
        raise NotImplementedError


class BEToENTranslator(BaseTranslator):
    """
    Translator for Braille to English.
    """
    LETTER_MAPPING: Dict[str, str] = {
        "O.....": 'a',
        "O.O...": 'b',
        "OO....": 'c',
        "OO.O..": 'd',
        "O..O..": 'e',
        "OOO...": 'f',
        "OOOO..": 'g',
        "O.OO..": 'h',
        ".OO...": 'i',
        ".OOO..": 'j',
        "O...O.": 'k',
        "O.O.O.": 'l',
        "OO..O.": 'm',
        "OO.OO.": 'n',
        "O..OO.": 'o',
        "OOO.O.": 'p',
        "OOOOO.": 'q',
        "O.OOO.": 'r',
        ".OO.O.": 's',
        ".OOOO.": 't',
        "O...OO": 'u',
        "O.O.OO": 'v',
        ".OOO.O": 'w',
        "OO..OO": 'x',
        "OO.OOO": 'y',
        "O..OOO": 'z',
    }

    NUM_MAPPING: Dict[str, str] = {
        "O.....": '1',
        "O.O...": '2',
        "OO....": '3',
        "OO.O..": '4',
        "O..O..": '5',
        "OOO...": '6',
        "OOOO..": '7',
        "O.OO..": '8',
        ".OO...": '9',
        ".OOO..": '0',
    }

    SPECIAL_MAPPING: Dict[str, str] = {
        "..OO.O": '.',
        "..O...": ',',
        "..O.OO": '?',
        "..OOO.": '!',
        "..OO..": ':',
        "..O.O.": ';',
        "....OO": '-',
        ".O..O.": '/',
        ".OO..O": '<',
        "O..OO.": '>',
        "O.O..O": '(',
        ".O.OO.": ')'
    }

    SPACE_BE = "......"
    SPACE_EN = " "

    CAPITAL_FOLLOWS = ".....O"

    DECIMAL_FOLLOWS = ".O...O"

    NUMBER_FOLLOWS = ".O.OOO"

    def translate(self, sentence: str) -> str:
        tokens: List[str] = self.tokenizer.tokenize(sentence)
        ret_seq: List[str] = []
        capital_follows = False
        number_follows = False
        # decimal_follows = False
        for token in tokens:
            # check special chars
            if token == self.CAPITAL_FOLLOWS:
                capital_follows = True
                continue
            elif token == self.NUMBER_FOLLOWS:
                number_follows = True
                continue
            # No specification in the usage of DECIMAL_FOLLOWS, so this part is disabled
            # elif tokenizer == self.DECIMAL_FOLLOWS:
            #     decimal_follows = True
            #     continue
            elif token == self.SPACE_BE:
                # do not interpret as number if a space is met.
                number_follows = False
                ret_seq.append(self.SPACE_EN)
            else:
                # check other types of token
                if number_follows:
                    if token in self.NUM_MAPPING:
                        ret_seq.append(self.NUM_MAPPING[token])
                    else:
                        raise ValueError("Unknown number token {}".format(token))
                else:
                    if token in self.LETTER_MAPPING:
                        ret_seq.append(
                            self.LETTER_MAPPING[token].capitalize() if capital_follows else self.LETTER_MAPPING[token])
                    elif token in self.SPECIAL_MAPPING:
                        ret_seq.append(self.SPECIAL_MAPPING[token])
                    else:
                        raise ValueError("Unknown letter token {}".format(token))
            # only capitalize the following one character
            capital_follows = False
        return ''.join(ret_seq)


class ENToBETranslator(BaseTranslator):
    """
    Translator for English to Braille.
    """
    LETTER_MAPPING: Dict[str, str] = {
        'a': "O.....",
        'b': "O.O...",
        'c': "OO....",
        'd': "OO.O..",
        'e': "O..O..",
        'f': "OOO...",
        'g': "OOOO..",
        'h': "O.OO..",
        'i': ".OO...",
        'j': ".OOO..",
        'k': "O...O.",
        'l': "O.O.O.",
        'm': "OO..O.",
        'n': "OO.OO.",
        'o': "O..OO.",
        'p': "OOO.O.",
        'q': "OOOOO.",
        'r': "O.OOO.",
        's': ".OO.O.",
        't': ".OOOO.",
        'u': "O...OO",
        'v': "O.O.OO",
        'w': ".OOO.O",
        'x': "OO..OO",
        'y': "OO.OOO",
        'z': "O..OOO",
    }

    NUM_MAPPING: Dict[str, str] = {
        '1': "O.....",
        '2': "O.O...",
        '3': "OO....",
        '4': "OO.O..",
        '5': "O..O..",
        '6': "OOO...",
        '7': "OOOO..",
        '8': "O.OO..",
        '9': ".OO...",
        '0': ".OOO..",
    }

    SPECIAL_MAPPING: Dict[str, str] = {
        '.': "..OO.O",
        ',': "..O...",
        '?': "..O.OO",
        '!': "..OOO.",
        ':': "..OO..",
        ';': "..O.O.",
        '-': "....OO",
        '/': ".O..O.",
        '<': ".OO..O",
        '>': "O..OO.",
        '(': "O.O..O",
        ')': ".O.OO."
    }

    SPACE_BE = "......"
    SPACE_EN = " "

    CAPITAL_FOLLOWS = ".....O"

    NUMBER_FOLLOWS = ".O.OOO"

    def translate(self, sentence: str) -> str:
        """
        Translate English sentence to Braille.
        :param sentence: English sentence
        :return: Braille sentence
        """
        tokens: List[str] = self.tokenizer.tokenize(sentence)
        ret_seq: List[str] = []
        number_follows = False
        for token in tokens:
            # if token is a letter
            if token.lower() in self.LETTER_MAPPING:
                if token.isupper():
                    ret_seq.append(self.CAPITAL_FOLLOWS + self.LETTER_MAPPING[token.lower()])
                else:
                    ret_seq.append(self.LETTER_MAPPING[token])
            # if token is a special char
            elif token in self.SPECIAL_MAPPING:
                ret_seq.append(self.SPECIAL_MAPPING[token])
            # if token is a digit
            elif token.isdigit():
                if not number_follows:
                    ret_seq.append(self.NUMBER_FOLLOWS + self.NUM_MAPPING[token])
                    number_follows = True
                else:
                    ret_seq.append(self.NUM_MAPPING[token])
                continue
            # token is a space
            elif token == self.SPACE_EN:
                ret_seq.append(self.SPACE_BE)
            else:
                raise ValueError("Invalid English token: {}".format(token))
            number_follows = False
        return ''.join(ret_seq)


def classify_language(sentence: str) -> Language:
    """
    Get the language type by the sentence provided

    :param sentence: a sentence in either English or Braille.
    :return: language enum of the provided sentence
    """
    return Language.BRAILLE if all(char in '.O' for char in sentence) else Language.ENGLISH


if __name__ == '__main__':
    """
    Entry point for the translator
    """
    # read console arguments
    input_sentence = ' '.join(sys.argv[1:])

    # recognize the language type
    lang = classify_language(input_sentence)

    # translate
    if lang == Language.ENGLISH:
        translator = ENToBETranslator(ENTokenizer())
    else:
        translator = BEToENTranslator(BETokenizer())
    # output result
    print(translator.translate(input_sentence))
