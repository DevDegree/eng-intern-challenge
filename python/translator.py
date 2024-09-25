import sys
from enum import Enum
from braille_to_char import CHAR_TO_BRAILLE as char2braille
from braille_to_char import NUM_TO_BRAILLE as num2braille
from functools import reduce

braille2char = {v: k for k, v in char2braille.items()}
braille2num = {v: k for k, v in num2braille.items()}

MISSING = "*"
SPACE = " "


class State(str, Enum):
    DEFAULT = "default"
    CAP = "capital"
    NUMBER = "number"
    DECIMAL = "decimal"


class MalformedInput(Exception):
    pass


def parse_braille(tokens):
    # lol spending too much time writing TS recently, closures ftw
    def look_around_num() -> bool:
        """If first char on either LHS or RHS is a number, then return true"""
        lhs_step, lhs_end = -1, 0
        rhs_step, rhs_end = 1, len(tokens) - 1

        for step, end in [(lhs_step, lhs_end), (rhs_step, rhs_end)]:
            k = 0
            while i + k != end:
                k += step
                if braille2char.get(tokens[i + k], MISSING) == SPACE:
                    continue
                if tokens[i + k] in braille2num.keys():
                    return True
                else:
                    return False
        return False

    state = State.DEFAULT
    output = ""

    for i in range(len(tokens)):
        # decimal and numbers are parsed the same way
        if state in [State.NUMBER, State.DECIMAL] and tokens[i] in braille2num.keys():
            char = braille2num[tokens[i]]
        else:
            # resolve collisions
            # 1. ? vs. decimal
            if braille2char.get(tokens[i], MISSING) == "decimal":
                if i > 0 and braille2char.get(tokens[i - 1], MISSING) == ".":
                    char = "decimal"
                else:
                    char = "?"
            # 2. > vs. o
            elif braille2char.get(tokens[i], MISSING) == ">":
                if look_around_num():
                    char = ">"
                else:
                    char = "o"
            else:
                char = braille2char.get(tokens[i], MISSING)
                if state == State.CAP:
                    char = char.upper()
                    state = State.DEFAULT

        # state transition
        if char in [State.CAP, State.NUMBER, State.DECIMAL]:
            state = char
            continue

        # Assumptions:
        # When in state NUMBER, SPACE is treated as an actual output token
        # rather than just being consumed as a control char to terminate the NUMBER state
        # This has consequences that the following inputs are essentially illegal:
        #   abc123abc -> abc123123 [mistranslation!]
        #
        # handle space terminating number state
        elif char == SPACE:
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
        elif tokens[i] == SPACE and state == State.NUMBER:
            state = State.DEFAULT
            bchar = tok2braille.get(tokens[i], tok2braille[MISSING])
        else:
            bchar = tok2braille.get(tokens[i], tok2braille[MISSING])

        output += bchar

    return output


def check_braille(chrs):
    return all([c in [".", "O"] for c in chrs])


def parse_arg(br_in: str, is_braille):
    tokens = []

    for i in range(0, len(br_in) - 1, 6):
        token = br_in[i : i + 6]
        tokens.append(token)

    if is_braille:
        out = parse_braille(tokens)
    else:
        out = parse_string(reduce(lambda x, y: x + y, tokens))

    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input supplied, exiting")
        sys.exit(0)

    args = sys.argv[1:]
    is_braille = check_braille("".join(args))
    SEPARATOR = SPACE if is_braille else char2braille[SPACE]

    print(f"{SEPARATOR}".join([parse_arg(arg, is_braille) for arg in args]))

    # str_tests = [
    #     ["hello world"],
    #     ["3 > 2"],
    #     ["5.2314"],
    #     ["abc123xyz"],
    #     ["hello 123 world"],
    #     ["1.23 < 4.56"],
    #     ["test? yes!"],
    #     ["a1b2c3"],
    #     ["3.14 > pi"],
    #     ["(start) 123 (end)"],
    #     ["1st 2nd 3rd"],
    #     ["a.b.c. 1.2.3"],
    #     ["100 > 90"],
    #     ["x-ray / z-axis"],
    #     ["q1: 1,234.56"],
    #     ["user: tag 123"],
    #     ["(a+b) / c = 123"],
    #     ["10:30 - 14:45"],
    #     ["isbn: 978-0-123456-47-2"],
    #     ["a1b2c3 > x1y2z3"],
    # ]
    # br_tests = []
    # for args in str_tests:
    #     is_braille = check_braille("".join(args))
    #     SEPARATOR = SPACE if is_braille else char2braille[SPACE]
    #     translated = f"{SEPARATOR}".join([parse_arg(arg, is_braille) for arg in args])

    #     print(f"Test Case {args}: ", translated)

    #     br_tests.append(
    #         [translated, args[0]]
    #     )  # Store original input along with Braille

    # print("\nBraille to Text Translation Tests:")
    # for braille, original in br_tests:
    #     is_braille = check_braille("".join(braille))
    #     SEPARATOR = SPACE if is_braille else char2braille[SPACE]

    #     translated = f"{SEPARATOR}".join(
    #         [parse_arg(arg, is_braille) for arg in [braille]]
    #     )

    #     # Compare translated result with original input
    #     if translated.lower() == original.lower():  # Case-insensitive comparison
    #         result = "PASS"
    #     else:
    #         result = "FAIL"

    #     print(f"Test Result: {result}")
    #     print(f"Original : {original}")
    #     print(f"Translated: {translated}")
    #     print("-" * 50)
