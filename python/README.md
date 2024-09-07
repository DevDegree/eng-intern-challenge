# Python Instructions

# Braille and English Translator

This application provides functionality to translate between Braille and English text. It is designed to work via the command line and perform the appropriate translation.

## Key Features

### Braille to English Translation
- **Functionality**: Translates Braille input to English text.
- **UPPERCASE Words**: Recognizes UPPERCASE words in Braille, indicated by two consecutive `CAPITAL_FOLLOWS` symbols. Note that this feature is not mirrored in the reverse translation.

### English to Braille Translation
- **Functionality**: Converts English text to Braille. 
- **Note**: The translation does not replicate UPPERCASE word handling present in Braille to English translation to simplify the process.

### Special Symbols Handling
- **Decimal and Number Symbols**: `DECIMAL_FOLLOWS` and `NUMBER_FOLLOWS` symbols are treated similarly in Braille translation.
- **Mathematical Operators**: Numbers followed by operators are treated as digits following the operator. This approach may have limitations with mixed numbers and text.

### Uncertainty Handling
- **Edge Cases**: The current implementation has some limitations, especially in complex mathematical expressions and ambiguous inputs. Future enhancements could include more sophisticated algorithms or language models.

## Usage

To use the translator, provide an input string via command-line arguments. The application will detect whether the input is Braille or English and perform the appropriate translation.

### Example

```
$ python python/translator.py Hello world
```

### Test cases used to check the correctness of this application
```
python python/translator.py .O.OOOOO.O........O.O...
```
**Expected:** 4 b

```
python python/translator.py .O.OOOOO.O.........O.OOOO.O...
```

**Expected:** 4 2

```
python python/translator.py .O.OOOO.O.....OO.OO..O..
```

**Expected:** 2.5

```
python python/translator.py .O...OO.O.....OO.OO..O..
```

**Expected:** 2.5

```
python python/translator.py .O...OO.O.....OO.OO..O........O.....
```

**Expected:** 2.5 a

```
python python/translator.py .O...OO.O.....OO.OO..O........O..OOO
```

**Expected:** 2.5 z

***Note: *** with this one I tested correctness of my mapping
```
python python/translator.py .O...OO.O.....OO.OO..O.............O.....OOO.OOOOO..OO.OOO.OO.O.OOO...OO.OOOO..OO.O.O.OOO.OOOOO.OOO.O.O..OO.OO.OO.OO..O.O.O.O.O...O..OOO...OO...O.OO..OOOO..OOO...
```
**Expected:** 2.5 YXWVUTSRQPONMLKJIHGF

```
python python/translator.py .O...O.OO.....OO.OO.OO..
```

**Expected: 9.8**

```
python python/translator.py .O...O.OO.....OO.OO.OO......OO....OO....OOOOO.....OO.O..OO..O.OO..
```

**Expected:** 9.8---6.:h



##### Some cases with uncertainty

```
python python/translator.py .O...OO.O.....OO.OO..O...O..O..O..O.O.O.....OO.OO..O..
```

**Expected:** 2.5//2.5

***We assume that characters which might be math operations will be followed with digits in most cases. Otherwise whitespaces should be specified.**

```
python python/translator.py .O...O.OO.....OO.OO.OO......OO....OO....OOO.....
```

**Expected:** 9.8---1
