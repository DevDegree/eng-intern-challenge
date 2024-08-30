# Python Instructions

NOTE: As far as I understand, the test case is wrong. It uses the following system:

```
NUM_TO_BRAILLE = {
    "0": "O.....",
    "1": "O.O...",
    "2": "OO....",
    "3": "OO.O..",
    "4": "O..O..",
    "5": "OOO...",
    "6": "OOOO..",
    "7": "O.OO..",
    "8": ".OO...",
    "9": ".OOO..",
}
```

The correct system is:

```
NUM_TO_BRAILLE = {
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
```