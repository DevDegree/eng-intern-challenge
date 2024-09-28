import sys

# Braille and English Translation Object
class BrailleTranslator():
    def __init__(self):

        # list of braille in order a-z + caps_lock, nums_lock, space
        self.braille_list = [
            "O.....",
            "O.O...",
            "OO....",
            "OO.O..",
            "O..O..",
            "OOO...",
            "OOOO..",
            "O.OO..",
            ".OO...",
            ".OOO..",
            "O...O.",
            "O.O.O.",
            "OO..O.",
            "OO.OO.",
            "O..OO.",
            "OOO.O.",
            "OOOOO.",
            "O.OOO.",
            ".OO.O.",
            ".OOOO.",
            "O...OO",
            "O.O.OO",
            ".OOO.O",
            "OO..OO",
            "OO.OOO",
            "O..OOO",
            ".....O",
            ".O.OOO",
            "......"
        ]

        # dictionary of all braille translations when not translating numbers
        self.chars = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        self.chars += ["cap_follows", "num_follows", " "]
        self.braille_char = dict(zip(self.braille_list, self.chars))

        # braille translation for numbers
        self.braille_nums = {
            "O.....": "1",
            "O.O...": "2",
            "OO....": "3",
            "OO.O..": "4",
            "O..O..": "5",
            "OOO...": "6",
            "OOOO..": "7",
            "O.OO..": "8",
            ".OO...": "9",
            ".OOO..": "0",
        }

    # Read in function, check for Braille or English, translate accordingly
    def ReadIn(self, inp):

        # Translate from Braille
        if set(inp).issubset({".", "O"}):
            result = self.BrailleToEnglish(inp)
        # Translate from English
        else:
            result = self.EnglishtoBraille(inp)

        return result


    # English to Braille translation function
    def EnglishtoBraille(self, inp):
        
        # Output
        result = ""

        # Num lock var
        nums_lock = False

        # Iterate characters in string
        for c in inp:
            # Ordinal value of character
            ordinal = ord(c)
            # If space character
            if ordinal == 32:
                result += self.braille_list[-1]
                # Turn off nums lock if on
                if nums_lock:
                    nums_lock = False
            # If lower case character
            elif ordinal >= 97 and ordinal <= 122:
                result += self.braille_list[ordinal - 97]
            # If upper case character
            elif ordinal >= 65 and ordinal <= 90:
                result += self.braille_list[-3]
                result += self.braille_list[ordinal - 65]
            # If number
            elif ordinal >= 48 and ordinal <= 57:
                # Turn on nums lock if not already on and add nums follow Braille
                if not nums_lock:
                    nums_lock = True
                    result += self.braille_list[-2]
                if ordinal == 48:
                    result += self.braille_list[9]
                else:
                    result += self.braille_list[ordinal - 49]
                
        return result

    # Braille to English translation function
    def BrailleToEnglish(self, inp):

        # Output
        result = ""

        # Initlize follow variables
        caps_lock = False
        nums_lock = False

        # Seperate input into 6 length segments for each braille symbol
        brailles = [inp[i:i+6] for i in range(0, len(inp), 6)]

        for b in brailles:
            # Check for follow cases
            # Turn on caps lock, switch off after 1 letter
            if self.braille_char[b] == "cap_follows":
                caps_lock = True
                continue
            # Turn on num lock, keep on until next space char
            elif self.braille_char[b] == "num_follows":
                nums_lock = True
                continue

            # Check for locks
            if nums_lock:
                # Check for space to end num lock
                if self.braille_char[b] == " ":
                    nums_lock = False
                    result += " "
                    continue
                else:
                    result += (self.braille_nums[b])
                    continue
            # Check for caps lock, turn off after letter
            elif caps_lock:
                result += self.braille_char[b].upper()
                caps_lock = False
                continue

            result += self.braille_char[b]
        return result

if __name__ == "__main__":
    # Initialize translator object
    translator = BrailleTranslator()
    # Collect input
    cmds = sys.argv[1:]
    inp = " ".join(cmds)
    # Translate
    result = translator.ReadIn(inp)
    # Output
    sys.stdout.write(result)