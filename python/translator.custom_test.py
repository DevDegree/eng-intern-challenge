import unittest
import subprocess
import string
import random

ENG_LETTERS = string.ascii_lowercase
PUNCT = ['.', ',', '?', '!', ':', ';', '-', '/', '<', '(', ')']
INTS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def random_int():
    return INTS[random.randint(0, len(INTS) - 1)]

def random_punct():
    return PUNCT[random.randint(0, len(PUNCT) - 1)]

def random_letter(no_o=False):
    letter = ENG_LETTERS[random.randint(0, len(ENG_LETTERS) - 1)]
    if random.random() > 0.8:
        letter = letter.upper()

    if letter == 'o' and no_o:
        return random_letter(no_o)

    return letter

def gen():
    inp = ''

    gen = True
    state = " " # " " for space, "1" for number, "a" for letter, "." for punctuation
    while gen:
        rand = random.random()
        if state == ".":
            inp += ' '
            state = ' '
        elif state == "1":
            if rand > 0.4:
                inp += random_int()
            elif rand > 0.1:
                inp += ' '
                state = ' '
            else:
                inp += random_punct()
                state = '.'
        elif state == "a":
            if rand > 0.2:
                inp += random_letter()
            elif rand > 0.05:
                inp += ' '
                state = ' '
            else:
                inp += random_punct()
                state = '.'
        else: # state = " "
            if rand > 0.3:
                inp += random_letter(no_o=True)
                state = "a"
            else:
                inp += random_int()
                state = "1"

        if random.random() < 0.02:
            gen = False

    return inp.strip()

class TestTranslator(unittest.TestCase):
    def test_output(self):
        RUNS = 1000

        for _ in range(RUNS):
            inp = gen()
            args = inp.split()

            command1 = ["python3", "translator.py"] + args

            #print(inp)
            
            result1 = subprocess.run(command1, capture_output=True, text=True)
            braille = result1.stdout.strip()

            #print(braille)

            command2 = ["python3", "translator.py"] + [braille]

            result2 = subprocess.run(command2, capture_output=True, text=True)
            eng = result2.stdout.strip()
            
            #print(eng)

            self.assertEqual(eng, inp)

if __name__ == '__main__':
    unittest.main()