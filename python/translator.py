from argparse import ArgumentParser


def main():
    args = get_args()
    print(args)


def get_args():
    parser = ArgumentParser("English <-> Braille translator")
    parser.add_argument("string", help="String to translate")

    return parser.parse_args()


if __name__ == "__main__":
    main()
