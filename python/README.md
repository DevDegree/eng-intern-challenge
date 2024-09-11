# Python Instructions

Note that the Python version used is 3.8

Usage: python3 translator.py string

Outputs translated string

Input validation:
- If string contains only `O` and `.` and has length divisible by 6, treat as Braille string
- Else if string contains only alphanumeric characters and spaces, treat as English string
- Otherwise, argument is invalid, output error message