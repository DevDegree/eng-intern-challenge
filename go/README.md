# Braille-English Translator

## Description

Created a Braille-English CLI translator using Go that automatically detects the input language (Braille or English) and converts it to the appropriate opposite language.

The application includes robust error management to ensure invalid inputs are appropriately flagged.

## Types of changes

- [ ] Bugfix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality not to work as expected)

## How Has This Been Tested?

- Initially tested using example inputs and outputs
- Created unit tests for edge cases:
  - Invalid Input (neither Braille nor English)
  - 'Invalid' Braille (string consisting of 'O's and '.'s but not following the specified Braille format).
  - Non-alphanumeric strings
  - The character following 'capital follows' must be a capital letter; otherwise, an error will be returned.
  - The character(s) following 'number follows' must be a number; otherwise, an error will be returned.
- Employed TDD principles, with unit tests created before writing the corresponding code, to ensure that all edge cases and expected behaviours were thoroughly covered.

## Checklist

- [x] Lint and unit tests pass locally with my changes
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] I have added the necessary documentation
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] My changes generate no new warnings

## Further comments

### Key Assumptions:

Braille must strictly consist of 'O's and '.'s. So if an arg contains a whitespace character, it is not valid Braille:

- './translator ...... ......' is valid since each arg does not have whitespace.
- './translator "...... ......"' is not valid since arg[1] has whitespace.

"capital follows" and "number follows" are reset when translating the next argument, i.e. if "capital follows" or "number follows" are still active in the preceding arg, they're reset for the current arg.

#### Braille to English:

Only letters are valid input when "capital follows" is active; otherwise, an error is returned.

Only numbers are valid input when "number follows" is active; otherwise, an error is returned.

#### English to Braille:

When numberFollows is active, and a letter is a current character, numberFollows becomes inactive, and a 'space' character is added to the result string, such that it precedes the current character.
