# Python Braille Translator

## Python Instructions

Note that the Python version used is 3.8

Run the tests using:
```bash
cd python
python3 translator.test.py
```

Run the program with your own inputs using:
```bash
cd python
python3 translator.py <text/braille>
```

## Assumptions

There are a number of edge cases that weren't addressed in the question that I made assumptions for.
1. At least one command line argument is passed to `translator.py` or else an error is raised.
2. Invalid characters raise an error instead of being skipped over.
3. Any braille input is only composed of valid braille cells (6 characters each).
4. All cells following a 'number follows' cell must be cells representing numbers. For example, a 'capital follows' cell cannot follow a 'number follows' cell (e.g. "13B").
5. Inputs are determined to be Braille or English based on whether or not they include the "." character. This is because all braille cells include at least one dot, and English characters only support letters, numbers, and spaces.