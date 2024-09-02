"""CLI application to translate messages between Braille and English.

--------------------------------------------------------------------------------
IMPORTANT
--------------------------------------------------------------------------------
I've created a companion repo to store my additional test cases
and documentation. This way, I don't accidentally break the
automated validation by modifying other files in this repo.

You can find the companion repo here:
https://github.com/callumcurtis/shopify-intern-challenge-harness
--------------------------------------------------------------------------------
"""

from __future__ import annotations


class CliMessageParser:

    def __init__(
        self,
        *,
        separator: str = " ",
        split_compound_args: bool = True,
    ):
        """
        Optional keyword arguments:
            separator: the character(s) to place between tokens in the output message.
            split_compound_args: whether to split quoted arguments containing multiple tokens.
        """
        self.separator = separator
        self.split_compound_args = split_compound_args

    def parse(self, args: list[str] | None = None):
        """Returns the message formed by the given cli arguments.

        The first argument is assumed to be the name of the script and
        is excluded from the message.

        Arguments:
            args: list of cli arguments
        """
        if not args:
            import sys
            args = sys.argv
        if self.split_compound_args:
            args = [
                arg
                for compound in args
                for arg in compound.split()
            ]
        return self.separator.join(args[1:])


if __name__ == "__main__":
    message_parser = CliMessageParser()
    message = message_parser.parse()
    print(message)

