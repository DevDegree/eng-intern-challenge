import sys

def translate(text):
    # TODO: if English then translate to Braille
    # TODO: if Braille then translate to English
    pass

if __name__ == "__main__":
    argvs = sys.argv
    text = argvs[1:]

    print(text)
    translate(text)