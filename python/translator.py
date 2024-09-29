
import argparse

from translate import translate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs="+", help="The message to translate. It can be English or Braille.")

    args = parser.parse_args()

    print(translate(args.message))


if __name__ == "__main__":
    main()

