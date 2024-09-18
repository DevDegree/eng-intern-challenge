# Python Instructions

Note that the Python version used is 3.8

There are several things to note:
1. I tried to format my code as formal as possible to simulate the code quality in a work environment. Here is the approach I applied:
 - avoid using hard-coded strings in code logic: constants are used to make sure changes can be done easily in future.
 - avoid allocation if not needed: braille to english table will not be generated if the user does not try to translate from braille to english.
 - use type checking: function input and output are type-checked to avoid compile time error (even though it is not enforced in Python, I still think it is a good practice as it improves the code readability).
 - the code follows [PEP 8 Python Style Guide](https://peps.python.org/pep-0008/)
  
2. Code is tested with python3.8
   
3. Special character case are not implmented in the code as it is [not required](https://github.com/DevDegree/eng-intern-challenge/issues/3#issuecomment-2320788869) in this challenge.
   
4. Several extra tests cases has been added myself to ensure code robustness (they are already in the `translator.py`, and can run the cases):
```Python
    # test cases
    # test case1: number
    assert(translator.translate(translator.translate("2213123")) == "2213123")
    # test case2: alphabets
    assert(translator.translate(translator.translate("adsFasdf")) == "adsFasdf")
    # test case3: alphabets with numbers
    assert(translator.translate(translator.translate("a1 b")) == "a1 b")
    # test case4: alphabets with numbers complex
    assert(translator.translate(translator.translate("dfkladfasdS1234567890 cpkldfsaj")) == "dfkladfasdS1234567890 cpkldfsaj")
    # test case5: alphabets with numbers
    assert(translator.translate("Abc 123 xYz") == ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
    # test case6: alphabets and numbers with other characters
    assert(translator.translate(translator.translate("dfkladfasd1234567890 cpkldfsJj;")) == "dfkladfasd1234567890 cpkldfsJj;")
    # test case7: english input but looks like braille
    assert(translator.translate(translator.translate("O......")) == "O......")

```
