# JavaScript Instructions

## Overview

A JavaScript Braille translator that converts text to Braille and vice versa. It supports letters, digits, and basic punctuation, including capitalization and numeric indicators.

## Logic

### Braille Map

The `brailleMap` object defines Braille representations for letters, digits, and special symbols:

- **Alphabet:** Letters are mapped to their Braille patterns.
- **Digits:** Digits 0-9 are represented in Braille with special mappings.
- **Special Symbols:** Includes capitalization and numeric indicators.

### Translation Function

The `translate` function handles both Braille-to-text and text-to-Braille conversions:

1. **Braille-to-Text:**
   - Checks if the input is Braille using a regex pattern.
   - Processes Braille input in chunks of 6 characters.
   - Detects and handles capitalization and numeric modes.
   - Converts each Braille pattern to its corresponding English character.

2. **Text-to-Braille:**
   - Converts each character of the input text to its Braille equivalent.
   - Handles numeric and capitalization indicators.
   - Constructs the Braille output string by appending Braille patterns for each character.

### Modes

- **Capitalization Mode:** Activated by the `cap` pattern, it converts the following letter to uppercase.
- **Numeric Mode:** Activated by the `num` pattern, it converts the following digits to their Braille representation.

