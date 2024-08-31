import sys


def main() -> None:
    if len(sys.argv) < 2:
        raise ValueError("Usage: python translator.py <argument>")

    chr_to_braille = {
        "a": "O.....",
        "b": "O.O...",
        "c": "OO....",
        "d": "OO.O..",
        "e": "O..O..",
        "f": "OOO...",
        "g": "OOOO..",
        "h": "O.OO..",
        "i": ".OO...",
        "j": ".OOO..",
        "k": "O...O.",
        "l": "O.O.O.",
        "m": "OO..O.",
        "n": "OO.OO.",
        "o": "O..OO.",
        "p": "OOO.O.",
        "q": "OOOOO.",
        "r": "O.OOO.",
        "s": ".OO.O.",
        "t": ".OOOO.",
        "u": "O...OO",
        "v": "O.O.OO",
        "w": ".OOO.O",
        "x": "OO..OO",
        "y": "OO.OOO",
        "z": "O..OOO",
    }
    num_to_braille = {
        "1": "O.....",
        "2": "O.O...",
        "3": "OO....",
        "4": "OO.O..",
        "5": "O..O..",
        "6": "OOO...",
        "7": "OOOO..",
        "8": "O.OO..",
        "9": ".OO...",
        "0": ".OOO..",
    }
    special_to_braille = {
        "capital": ".....O",
        "number": ".O.OOO",
        " ": "......",
    }

    braille_to_chr = {v: k for k, v in chr_to_braille.items()}
    braille_to_num = {v: k for k, v in num_to_braille.items()}
    braille_to_special = {v: k for k, v in special_to_braille.items()}

    all_brailles = set(braille_to_chr) | set(braille_to_num) | set(braille_to_special)

    input_str = " ".join(sys.argv[1:])

    # check if the input_str is letters or braille. If braille, will return list of brailles.
    def is_braille(s):
        if len(s) % 6 == 0:
            brailles = [s[i : i + 6] for i in range(0, len(s), 6)]
            return brailles if all(b in all_brailles for b in brailles) else False
        return False

    braille_str = is_braille(input_str)
    output, is_num, is_capital = "", False, False

    if braille_str:  # when the input is braille
        for b in braille_str:
            if is_num and b in braille_to_num:
                output += braille_to_num[b]
            else:
                if b in braille_to_special:
                    if is_capital:
                        raise ValueError(
                            "Should be follwed by alphabet letter after 'capital follows' braille"
                        )
                    if braille_to_special[b] == "capital":
                        is_capital = True
                    elif braille_to_special[b] == "number":
                        is_num = True
                    else:
                        output += braille_to_special[b]
                        is_num = False
                else:
                    output += (
                        braille_to_chr[b].upper() if is_capital else braille_to_chr[b]
                    )
                    is_capital = False
    else:  # when input is alphabet, number, or space character.
        for c in input_str:
            if c.isalpha():
                if c.isupper():
                    output += special_to_braille["capital"]
                output += chr_to_braille[c.lower()]
            elif c.isnumeric():
                if not is_num:
                    output += special_to_braille["number"]
                    is_num = True
                output += num_to_braille[c]
            elif c in special_to_braille:
                output += special_to_braille[" "]
                is_num = False
            else:
                raise ValueError(
                    "Input character is not valid. Acceptable inputs include : alphabet letters, numbers, and space"
                )

    print(output)


if __name__ == "__main__":
    main()
