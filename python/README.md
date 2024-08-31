# Python Instructions

Note that the Python version used is 3.8

## Assumptions
* All inputs are valid according to the technical specifications
  * all English inputs only contain `0-9`, `a-z`, `A-Z` and/or `space`
* Braille inputs are exactly those that are:
  * characters are all `O` or `.`
  * has length that is multiple of 6 (since all Braille cells are 6 characters long)
  * has ≥1 `.` (since all given Braille cells have at least 1 non-raised dot, and translating `.` was not part of the technical requirements)
* Capital follows only affects the character that directly follows, even if it cannot be capitalized (ie. is a space)