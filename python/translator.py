import sys

class BrailleTranslator:
    """
    Class for automatically detecting and applying English <-> Braille translation.
    """

    def __init__(self):
        """
        Initialize the MainClass with a name.
        :param name: The name for this instance.
        """

    def greet(self):
        """
        Greet with the name provided.
        """
        print(f"Hello, {self.name}!")

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <english/braille>")
        sys.exit(1)
    
    translator = BrailleTranslator()
    
    

if __name__ == "__main__":
    main()
