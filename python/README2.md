# Run

To run the Python program which can convert Braille to English or vice-versa. Simply run this in terminal

```
python translator.py your_text_to_translate
```

# Complexity

The solutiont takes O(n) time to translate. Where n is the length of the string to translate.


# Notes

- The solution cannot handle two or more spaces between words. For example "Hello&nbsp;&nbsp;&nbsp;&nbsp;World" will be interpreted as "Hello World". An easy fix for this would be to take arguments as a string in the program.
- It also cannot handle just space as input. Right now, it just returns space. Ideally, it should return `......`.  
- Decimals, brackets, comparison operators, slash, punctuations are not supported in the solution. 
- The third example provided in README.md is might be `Abc 234` instead of the given `Abc 123`. 
- As per the given test case and conditions, the input `Hello123Wello` is not possible to be converted to Braille. Since we need a space before we can start the alphabets from numbers. Had we interpreted the question differently and had rather read space as the stopper for numbers, then an additional space character to show space would have been required and the test case provided in `translator.test.py` would have failed. Therefore, the former assumption has been considered by me while writing the solution. 
