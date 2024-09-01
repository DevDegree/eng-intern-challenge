# Python Instructions

Note that the Python version used is 3.8

### Testing

Test with my new testing by invoking `python3 -m unittest` from within the Python directory.

### Notes & TODOs

NOTE - For ambiguous cases, assumes Braille (ex: O.O.O. would be considered Braille, not English.)

NOTE - Currently '>' is considered a numeric character, since the braille Key for '>' is identical to that for 'o'. Therefore, if the context is numeric, > is used, and otherwise, 'o' is used.

NOTE - Currently this is a converter from Braille to Alphanumeric.
TODO - Enforce english-only.

TODO - Add verbose logging.
TODO - Stronger help message
TODO - Logging for when a key-error occurs on conversions (invalid character inputs)
