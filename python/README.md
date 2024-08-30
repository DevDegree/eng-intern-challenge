# Python Instructions

Note that the Python version used is 3.8

## Running

```
python translator.py <braille or text string>
```

## Assumptions

* Length of **braille string** provided is divisible by 6
* **"Invalid cases" are omitted:**
    * eg. input such as "0a" is not possible because there must be a space (......) braille character in order to stop interpreting braille numerically
    * Only valid text is provided - eg. alphanumeric characters `a-z`, `A-Z`, and `0-9` (no punctuation or special chars)
    * A string is determined to be braille if it contains a '.' character *(periods in English text not included) in problem*
* **From technical requirements:**
    * "When a Braille capital follows symbol is read, assume only the next symbol should be capitalized."
    * "When a Braille number follows symbol is read, assume all following symbols are numbers until the next space symbol."

### Written by Andrew Verbovsky for the Shopify Eng Intern challenge Fall - Winter 2025