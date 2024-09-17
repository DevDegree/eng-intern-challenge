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
  "CF": ".....O", // Capital letter follows
  "NF": ".O.OOO", // Number follows
  "DF": ".O...O", // Decimal follows
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

// Function to translate between braille and normal text
const translate = (input) => {
  const isBraille = input.split('').every(char => ['O', '.'].includes(char));

  if (isBraille) {
    // return brailleToText(input);
  } else {
    // return textToBraille(input);
  }
}