from translator import english_to_braille, braille_to_english
from colorama import Fore, Style

english_sentences = [
    "Hello World",
    "This is a test",
    "Python programming",
    "Braille translation",
    "Numbers 12345",
    "Numbers 67890",
    "Special characters: !, ?, ;",
    "  Leading space",
    "Trailing space ",
    "  Multiple spaces  inside",
    "Punctuation. at the end.",
    "23 The Quick Brown 43 Fox23 Jumps Over THe Lazy Dog",
    "123 abc456 def",
    "Numbers 123 456 789 and words",
    "M1 xed CASE2 sentence3 with4 numbers",
]

def test_translation(sentences):
    passedAll = True
    for sentence in sentences:
        braille = english_to_braille(sentence)
        translated_back = braille_to_english(braille)
        match = sentence == translated_back
         
        if not match:
            passedAll = False 
            print(f"Original: {sentence}")
            print(f"Braille: {braille}")
            print(f"Translated back: {translated_back}")
            print(f"{Fore.RED}Match: {match}{Style.RESET_ALL}")
            print("-" * 30)
    
    if passedAll:
        print(f"{Fore.GREEN}All tests passed{Style.RESET_ALL}")

test_translation(english_sentences)
