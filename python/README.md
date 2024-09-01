# Python Instructions

Note that the Python version used is 3.8

## How To Run (w/o test)
1. CD into the `/python` directory
2. Run `python3 translator.py Your String Here`
#### Depending on if the string is in braille format or normal text, the text will be converted to the other type of string (Braille to English or English to Braille)

## How To Run (using test)
1. CD into the `/python` directory
2. Run `python3 translator.test.py`
3. Test will return `OK` if it has passesd, else `FAILED` otherwise

## How it Works
1. When the arguments are passed in to the CLI, the program decides if there are sufficent arguments provided
2. It will then use a specific `regex` pattern to determine if the input it braille or not
3. If the input is in braille, it attempts to convert it to English, otherwise the input is English, and will therefore convert it to braille
4. Using a `dict/hashmap` the input text will be matched to the equivalent pair and returned as a new `string`

- Note: if no "*correct*" arguments are passed in, the program will return an error