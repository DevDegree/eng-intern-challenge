# Python Instructions
This file converts braille to English and vice versa.

brailles_constant.py This file holds all the constants needed for the program to run.
brailles_functions.py This file holds all the functions needed for the program to run.
    It requires the constants file to run.
    It has a function is_braille that determines if the given input or braille or english.
    It has another function poof_braille that converts english to braille.
        this function uses loops and constants dictionaries to convert to braille. Ecxeptions such as decimal period and other such characters are handled.
    It has another function poof_english that converts braille to english.
        this function uses loops and constants dictionaries to convert to english. Ecxeptions such as decimal period and other such characters are handled.

translator.py is a file where everyhting comes together. function calls are made and the program runs.

translator.test.py is a file where the program is tested. 
encounter any isses: solution
    make sure for line number 8 in this file you have the correct path and version.
    command = [sys.executable, "python/translator.py", "Abc", "123", "xYz"] # I changed it to sys.executable so it would work better for me for compatibility.
    intead of python3 sys.executable works way better in order to run the program and counter incompatibility issues. 
    If you cd python in the python folder and keep the tests the same as designed that should work perfectly as well. 


to run the program use the command:
example of mine: 
/opt/homebrew/bin/python3 /Users/diyapatel/translator_assignment/eng
-intern-challenge/python/translator.test.py

where your python3 is located. location/file.py
