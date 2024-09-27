import sys


def is_braille(text):
    """Checks if the input is Braille (valid Braille symbols)."""
    return all(c in 'O.' for c in text) and len(text) % 6 == 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python translator.py <text>")
        sys.exit(1)

    input_text = sys.argv[1]
    if is_braille(input_text):
        # Translate Braille to English
        print("Braille")
    else:
        # Translate English to Braille
        print("English")
