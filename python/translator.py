import sys

class BrailleTranslator:
    def __init__(self):

        # Dictionnaire pour la conversion des lettres en braille
        # Dictionary for letter-to-braille conversion
        self.braille_dict = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
            'z': 'O..OOO', ' ': '......', 'capital': '.....O'
        }

        # Dictionnaire pour les chiffres en braille
        # Dictionary for number-to-braille conversion
        self.number_dict = {
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
        }
        # Indicateur pour les chiffres en braille
        # Number indicator in braille
        self.number_indicator = '.O.OOO'

        # Dictionnaire inversé pour la conversion du braille vers l'anglais (lettres)
        # Reverse dictionary for braille-to-letter conversion
        self.reverse_braille_dict = {v: k for k, v in self.braille_dict.items()}

        # Dictionnaire inversé pour la conversion du braille vers l'anglais (chiffres)
        # Reverse dictionary for braille-to-number conversion
        self.reverse_number_dict = {v: k for k, v in self.number_dict.items()}

    def is_braille(self, text):
        """Vérifie si la chaîne contient uniquement des caractères braille (O et .)
        Check if the string contains only braille characters (O and .)
        """
        return all(c in 'O.' for c in text)

    def from_braille(self, braille):
        """
        Traduit une chaîne de caractères en braille en texte anglais.

        Args:
            braille (str): Chaîne en braille à traduire.

        Returns:
            str: Texte traduit en anglais.
        """
        """
        Translates a braille string to English text.

        Args:
            braille (str): Braille string to translate.

        Returns:
            str: Translated English text.
        """
        result = ""
        is_capital = False  # Indicateur pour les majuscules Flag for capital letters
        number_mode = False  # Indicateur pour les chiffres  Flag for numbers

        # Divise la chaîne braille en groupes de 6 caractères
        # Split braille string into groups of 6 characters
        braille_chars = [braille[i:i + 6] for i in range(0, len(braille), 6)]

        for char in braille_chars:
            if char == '.....O':
                is_capital = True
            elif char == '......':
                result += ' '
                number_mode = False  # Réinitialiser le mode numérique après un espace   Reset number mode after a space
            elif char == self.number_indicator:
                number_mode = True
            else:
                if number_mode:
                    # Convertir le braille en chiffre
                    # Convert braille to number
                    letter = self.reverse_number_dict.get(char, '?')
                    result += letter
                else:
                    # Convertir le braille en lettre
                    # Convert braille to letter
                    letter = self.reverse_braille_dict.get(char, '?')
                    result += letter.upper() if is_capital else letter
                    is_capital = False  # Réinitialiser après utilisation  Reset after use

        return result

    def to_braille(self, text):
        """
        Traduit une chaîne de caractères anglais en braille.

        Args:
            text (str): Chaîne en anglais à traduire.

        Returns:
            str: Texte traduit en braille.
        """
        """
                Translates an English string to braille.

                Args:
                    text (str): English string to translate.

                Returns:
                    str: Translated braille text.
                """
        result = ""
        is_number_mode = False

        for char in text:
            if char.isdigit():
                if not is_number_mode:
                    result += self.number_indicator  # Ajouter l'indicateur de chiffre  Add number indicator
                    is_number_mode = True
                result += self.number_dict[char]
            else:
                if is_number_mode:
                    is_number_mode = False  # Réinitialiser après un chiffre Reset after number
                if char.isupper():
                    result += self.braille_dict['capital'] + self.braille_dict[char.lower()]
                else:
                    result += self.braille_dict.get(char, '......')  # Gérer les caractères inconnus comme espace/ Handle unknown characters as space
        return result

    def translate(self, input_text):
        """Traduit le texte, en détectant automatiquement si c'est du braille ou de l'anglais."""
        "Automatically detects if the text is in braille or English and translates it."
        if self.is_braille(input_text):
            return self.from_braille(input_text)
        else:
            return self.to_braille(input_text)


def main():
    # On combine tous les arguments passés en une seule chaîne de texte
    #  We Combine all passed arguments into one text string
    input_text = " ".join(sys.argv[1:])
    translator = BrailleTranslator()
    output = translator.translate(input_text)
    print(output)


if __name__ == "__main__":
    main()
