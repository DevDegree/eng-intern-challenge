# Python Instructions

Note that the Python version used is 3.8


# Eng Intern Challenge Fall- Winter 2025 Python solution

Hello! The following is just a run-down, and additional context for my solution to the challenge.

## Intution

Looking at the Braille image provided, it comes immediately to mind that the There is a 1:1 mapping of English letters and symbols to their appropriate braille cells, making a key-value realtionship (ignoring the `>` and `<` symbols as they are incorrect).

![Braille Alphabet image](/braille.jpg)

The letters can be keys, and the cells can be values in a dictionary, or vice versa.

This brings the main idea of mapping each letter, symbol, and indicator to their own value or key, and referencing the dictionary for translation.


## Processes

Without writing too much detail, there are three main things which need to happen to complete this challenge:

1. The program must detect what system (English or Braille) is being used.
2. The program must be able to translate to English if Braille is provided.
3. The program must be able to translate to Braille if English is provided.


This brings the idea of mapping each one of these to a function, leading to the functions:

1. `detect_system()`
2. `translate_braille()`
3. `translate_english()`

Then all of them are combined within the main function to process inputed arguments for the challenge.

## Notes

* Whilst I could have only one set of dictionaries mapping English -> Braille, I figured some memory could be traded off for a more efficient runtime, otherwise thee maps could be reversed as such
`braille_to_alphabet = {v: k for k, v in alphabet_to_braille.items()}`

* Looking at the logic to write a number down, there is technically a "flaw" if there is no space after a number to end number processing, but I believe the assumption is that a "proper" English string is fed in.

* Fun fact: Whilst completing this challenge, I actually did not have an active internet connection as I was travelling. I however did get to clone the repo before technical requirements were clarified, which is why the symbols are included within the translator, bonus feature I guess?