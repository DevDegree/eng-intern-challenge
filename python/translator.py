import sys
from enum import Enum
from braille_to_char import CHAR_TO_BRAILLE as char2braille
from braille_to_char import NUM_TO_BRAILLE as num2braille
from functools import reduce

braille2char = {v: k for k, v in char2braille.items()}
braille2num = {v: k for k, v in num2braille.items()}

MISSING = "*"


class State(str, Enum):
    DEFAULT = "default"
    CAP = "capital"
    NUMBER = "number"
    DECIMAL = "decimal"


class MalformedInput(Exception):
    pass


def parse_braille(tokens):
    state = State.DEFAULT
    output = ""

    for i in range(len(tokens)):
        # decimal and numbers are parsed the same way
        if state in [State.NUMBER, State.DECIMAL] and tokens[i] in braille2num.keys():
            char = braille2num[tokens[i]]
        elif state == State.CAP:
            char = char.upper()
            state = State.DEFAULT
        else:
            # resolve collisions
            # 1. ? vs. decimal
            if tokens[i] == char2braille["?"]:
                if i > 0 and braille2char.get(tokens[i - 1], MISSING) == ".":
                    char = "decimal"
                else:
                    char = "?"
            # 2. > vs. o
            elif tokens[i] == char2braille[">"]:
                if tokens[i - 1] == " " and tokens[i + 1] in [
                    State.NUMBER,
                    State.DECIMAL,
                ]:
                    char = ">"
                else:
                    char = "o"
            else:
                char = braille2char.get(tokens[i], MISSING)

        # state transition
        if char in [State.CAP, State.NUMBER, State.DECIMAL]:
            state = char
            continue
        # handle space terminating number state
        elif char == char2braille[" "]:
            if state in (State.NUMBER, State.DECIMAL):
                state = State.DEFAULT

        output += char

    return output


def parse_string(tokens: str):
    tok2braille = char2braille | num2braille
    state = State.DEFAULT
    output = ""

    for i in range(len(tokens)):
        if tokens[i].isdigit():
            if state != State.NUMBER:
                bchar = tok2braille[State.NUMBER] + tok2braille[tokens[i]]
                state = State.NUMBER
            else:
                bchar = tok2braille[tokens[i]]
        elif tokens[i].isupper():
            bchar = tok2braille[State.CAP] + tok2braille[tokens[i].lower()]
        else:
            bchar = tok2braille.get(tokens[i], tok2braille[MISSING])
            if bchar == " " and state == State.NUMBER:
                state = State.DEFAULT

        output += bchar

    return output


def check_braille(chrs):
    return all([c in [".", "O"] for c in chrs])


def parse_arg(br_in: str):
    tokens = []
    is_braille = True

    for i in range(0, len(br_in) - 1, 6):
        token = br_in[i : i + 6]
        tokens.append(token)
        is_braille = check_braille(token)

    if is_braille:
        out = parse_braille(tokens)
    else:
        out = parse_string(reduce(lambda x, y: x + y, tokens))

    sys.stdout.write(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input supplied, exiting")
        sys.exit(0)

    sys.stdout.write(" ".join([parse_arg(arg) for arg in sys.argv[1:]]))
