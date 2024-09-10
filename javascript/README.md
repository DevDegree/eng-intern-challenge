#   Braille Translator

This is a terminal-based command-line application that translates between Braille and English. The application automatically detects whether the input is Braille or English and converts it accordingly.

##  How to Run the Application
Install the dependencies 

For example, for JavaScript:

```
npm install
```
Run the application:

The input can either be in English or Braille.
The application will output the translated string directly to the console.
Example Commands:
To translate from English to Braille:

```
node translator.js "Hello world"
```
To translate from Braille to English:

```
node translator.js ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
```

Translating numbers:

```
node translator.js "42"

```
##  Input/Output Examples:

### Input: "Hello world"


### Output:

![image](https://github.com/user-attachments/assets/1f31230a-3fab-4b39-8fa1-c5c9df9fe589)

### Input:
```
 ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....
```

### Output:
![image](https://github.com/user-attachments/assets/d310f188-885c-4c9d-af1b-7dc54bcd1fd7)


### Test Case 
#### Input
```
node translator.js Abc 123 xYz
```
#### Output 
![image](https://github.com/user-attachments/assets/f983bda2-5084-478f-b6fd-53d90565befe)


Comparing outputs 
![image](https://github.com/user-attachments/assets/62be49a8-1867-4c90-803a-6118f7071fa5)



### Features
1.  Supports the entire English alphabet (a-z).
Translates both capital letters and lowercase letters.
2.  Handles spaces between words.
3.  Supports numbers 0-9, with Braille number mode.
4.  Automatically detects if the input is Braille or English.

### Technical Details
Each Braille character is represented by a 6-character string of O (raised dots) and . (flat dots).
When a capital indicator follows a Braille character, only the next character is capitalized.
When a number indicator follows a Braille character, all subsequent characters are interpreted as numbers until the next space.

**Note:** The ">" character is not supported as per the project requirements. This is because the Braille code for the ">" character matches the Braille code for the letter "O", which leads to ambiguity in translation.
