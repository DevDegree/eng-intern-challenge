// Braille Alphabet Object
const brailleAlphabet = {
  "a": "O.....", 
  "b": "O.O...", 
  "c": "OO....", 
  "d": "OO.O..", 
  "e": "O..O..",
  "f": "OOO...", 
  "g": "OOOO..", 
  "h": "O.OO..", 
  "i": ".OO...", 
  "j": ".OOO..",
  "k": "O...O.", 
  "l": "O.O.O.",
  "m": "OO..O.", 
  "n": "OO.OO.", 
  "o": "O..OO.",
  "p": "OOO.O.", 
  "q": "OOOOO.", 
  "r": "O.OOO.", 
  "s": ".OO.O.", 
  "t": ".OOOO.",
  "u": "O...OO", 
  "v": "O.O.OO", 
  "w": ".OOO.O", 
  "x": "OO..OO", 
  "y": "OO.OOO", 
  "z": "O..OOO", 
  "CF": ".....O", // Capital letter follows
  "NF": ".O.OOO", // Number follows
  " ": "......",  // Space
  ".": "..OO.O", 
  ",": "..O...", 
  "?": "..O.OO", 
  "!": "..OOO.", 
  ":": "..OO..", 
  ";": "..O.O.", 
  "-": "....OO", 
  "/": ".O..O.", 
  "<": ".OO..O", 
  ">": "O..OO.",
  "(": "O.O..O", 
  ")": ".O.OO."
};

const brailleNumbers = {
  "1": "O.....", 
  "2": "O.O...", 
  "3": "OO....", 
  "4": "OO.O..", 
  "5": "O..O..", 
  "6": "OOO...", 
  "7": "OOOO..", 
  "8": "O.OO..", 
  "9": ".OO...", 
  "0": ".OOO..", 
  "DF": ".O...O", // Decimal follows
}

// reverse braille alphabet key and value for braille text conversion
const reverseBrailleAlphabet = Object.fromEntries(
  Object.entries(brailleAlphabet).map(([key, value]) => [value, key])
);

// reverse braille alphabet key and value for braille text conversion
const reverseBrailleNumbers = Object.fromEntries(
  Object.entries(brailleNumbers).map(([key, value]) => [value, key])
);

// Helper function - braille to text
const brailleToText = (brailleStr) => {
  const output = [];
  let isCapital = false;
  let isNumber = false;
  let i = 0;

  while (i < brailleStr.length) {
    let brailleChar = brailleStr.slice(i, i + 6);

    if (brailleChar === brailleAlphabet['CF']) {
      isCapital = true;
      i += 6;
      continue;
    }
    
    if (brailleChar === brailleAlphabet['NF']) {
      isNumber = true;
      i += 6;
      continue;
    }

    // conditionally checks if the character should check in alpha or number object
    let char = isNumber ? reverseBrailleNumbers[brailleChar] : reverseBrailleAlphabet[brailleChar];
    
    if (isCapital) {
      char = char.toUpperCase();
      isCapital = false;
    }

    if (isNumber) {
      if (char >= '0' && char <= '9') {
        output.push(char);
      } else if (char === 'DF') {
        output.push('.')
      } else {
        isNumber = false;
        output.push(' ');
      }
    } else {
      output.push(char);
    }

    i += 6;
  }

  return output.join('');
}

// Function to translate between braille and normal text
const translate = (input) => {
  const isBraille = input.split('').every(char => ['O', '.'].includes(char));

  if (isBraille) {
    return brailleToText(input);
  } else {
    // return textToBraille(input);
  }
}

// Input: Hello world
// Output: .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

// Input: 42
// Output: .O.OOOOO.O..O.O...

// Input: .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
// Output: Abc 123
console.log(translate('.....OO.....O.O...OO...........O.OOOO.....O.O...OO....'))

// 166.66 aa
console.log(translate('.O.OOOO.....OOO...OOO....O...OOOO...OOO.........O.....O.....'))