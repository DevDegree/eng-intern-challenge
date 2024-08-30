/* 
Create hashmaps:
  Braille to English keys:
    - letters + spaces + capital follows + number follows
    - numbers + spaces
  English to Braille keys:
    - letters + numbers + spaces

Main function:
  Determine if string argument is Braille or English
    If length of string < 6, it is English
    Else, search for first 6 characters of string in Braille to English hashmap(s)
      If in hashmaps, string is in Braille
        Pass string to appropriate translator function
      Else, string is in English
        Pass string to appropriate translator function

Braille to English translator function:
  Create isCapital and isNumber variables
  Create output variable
  Iterate over string, taking in 6 characters at a time
    Translate string.substr(i, i + 5) from Braille to English using hashmap
    Add translated character to output
    Continue iterating until end of string is reached
  Output translated string

English to Braille translator function:
  Create capitalSymbol and numberSymbol variables
  Create numberMode variable
  Create output variable
  Iterate over string, 1 character at a time
    If string[i] is a capital letter
      Add isCapital symbol to output
      Take lowercase string[i] and add its respective Braille symbol to output
    Else if string[i] is a number
      If numberMode === false
        Set numberMode = true
        Add isNumber symbol to output
      Add respective Braille symbol for string[i] to output
    Else (string[i] === ' ')
      Set numberMode = false
      Add Braille symbol for space to output
  Output translated string
*/

const brailleAlphabet = [
  { brl: 'O.....', eng: 'a', type: 'letter' },
  { brl: 'O.O...', eng: 'b', type: 'letter' },
  { brl: 'OO....', eng: 'c', type: 'letter' },
  { brl: 'OO.O..', eng: 'd', type: 'letter' },
  { brl: 'O..O..', eng: 'e', type: 'letter' },
  { brl: 'OOO...', eng: 'f', type: 'letter' },
  { brl: 'OOOO..', eng: 'g', type: 'letter' },
  { brl: 'O.OO..', eng: 'h', type: 'letter' },
  { brl: '.OO...', eng: 'i', type: 'letter' },
  { brl: '.OOO..', eng: 'j', type: 'letter' },
  { brl: 'O...O.', eng: 'k', type: 'letter' },
  { brl: 'O.O.O.', eng: 'l', type: 'letter' },
  { brl: 'OO..O.', eng: 'm', type: 'letter' },
  { brl: 'OO.OO.', eng: 'n', type: 'letter' },
  { brl: 'O..OO.', eng: 'o', type: 'letter' },
  { brl: 'OOO.O.', eng: 'p', type: 'letter' },
  { brl: 'OOOOO.', eng: 'q', type: 'letter' },
  { brl: 'O.OOO.', eng: 'r', type: 'letter' },
  { brl: '.OO.O.', eng: 's', type: 'letter' },
  { brl: '.OOOO.', eng: 't', type: 'letter' },
  { brl: 'O...OO', eng: 'u', type: 'letter' },
  { brl: 'O.O.OO', eng: 'v', type: 'letter' },
  { brl: '.OOO.O', eng: 'w', type: 'letter' },
  { brl: 'OO..OO', eng: 'x', type: 'letter' },
  { brl: 'OO.OOO', eng: 'y', type: 'letter' },
  { brl: 'O..OOO', eng: 'z', type: 'letter' },
  { brl: 'O.....', eng: '1', type: 'number' },
  { brl: 'O.O...', eng: '2', type: 'number' },
  { brl: 'OO....', eng: '3', type: 'number' },
  { brl: 'OO.O..', eng: '4', type: 'number' },
  { brl: 'O..O..', eng: '5', type: 'number' },
  { brl: 'OOO...', eng: '6', type: 'number' },
  { brl: 'OOOO..', eng: '7', type: 'number' },
  { brl: 'O.OO..', eng: '8', type: 'number' },
  { brl: '.OO...', eng: '9', type: 'number' },
  { brl: '.OOO..', eng: '0', type: 'number' },
  { brl: '.....O', eng: 'capitalFollows', type: 'follows' },
  { brl: '.O.OOO', eng: 'numberFollows', type: 'follows' },
  { brl: '......', eng: ' ', type: 'space' },
];

const brailleLettersMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'letter' || type === 'follows' || type === 'space') {
    brailleLettersMap.set(brl, eng);
  }
});

const brailleNumbersMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'number' || type === 'space') {
    brailleNumbersMap.set(brl, eng);
  }
});

const englishMap = new Map();
brailleAlphabet.forEach(({ brl, eng, type }) => {
  if (type === 'letter' || type === 'number' || type === 'space') {
    englishMap.set(eng, brl);
  }
});
