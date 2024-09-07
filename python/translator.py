import argparse, re

class translator:
    def __init__(self) -> None:

        parser = argparse.ArgumentParser(description='Translate a string into braille or braille to text.')

        parser.add_argument('BrailleOrText', type=str)

        givenArgument = parser.parse_args()

        # set up regex
        pattern = r'^(?=.*[O.])[O.]{2,}$'
        compiledPattern = re.compile(pattern)
        if re.match(compiledPattern, givenArgument.BrailleOrText):
            print("braille") # we will call corresponding functions from here
        else:
            print("text")

        self.text = givenArgument.BrailleOrText # we will only take the first argument because that's all that matters to us

    




if __name__ == "__main__":
    translatorObject = translator()


