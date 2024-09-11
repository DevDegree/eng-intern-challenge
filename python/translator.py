import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python translator.py <text>")
        return
    args = sys.argv[1:]
    input_text = " ".join(args)


if __name__ == "__main__":
    main()
