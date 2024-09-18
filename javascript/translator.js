const englishToBraille = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
  " ": "......",
};

const brailleToEnglish = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "......": " ",
};

const capitalMarker = ".O..OO";
const numberMarker = ".O.OOO";

const isBraille = function(input) {
  return /^[O.]+$/.test(input) && input.length % 6 === 0; //Checks if the input is a Braille string, only 'O' and '.'
};

const translate = function(input) {
  if (isBraille(input)) {
    return translateBrailleToEnglish(input);
  } else {
    return translateEnglishToBraille(input);
  }
};

const translateEnglishToBraille = function(input) {
  let result = "";
  let isNumberMode = false;

  for (let char of input) {
    if (char >= "A" && char <= "Z") {
      result += capitalMarker + englishToBraille[char.toLowerCase()]; // Converts to lowercase and adds capital marker
    } else if (char >= "0" && char <= "9") {
      if (!isNumberMode) {
        
        result += numberMarker;        // Adds number marker if not in number mode
        isNumberMode = true;
      }
      result += englishToBraille[char];
    } else if (char === " ") {
      isNumberMode = false;             // Reset number
      result += englishToBraille[char];
    } else {
      isNumberMode = false;
      result += englishToBraille[char];
    }
  }

  return result;
};

const translateBrailleToEnglish = function (input) {
  let result = "";
  let isNumberMode = false;
  let i = 0;

  while (i < input.length) {
    let brailleChar = input.substring(i, i + 6);

    if (brailleChar === capitalMarker) {      // Capitalize the next character
      

      i += 6;      // Move to the next Braille character
      brailleChar = input.substring(i, i + 6);
      let char = brailleToEnglish[brailleChar];
      if (char) {
        result += char.toUpperCase();
      }
    } else if (brailleChar === numberMarker) {       // Switch to number mode
      

      isNumberMode = true;
    } else if (brailleChar === "......") {   // Space and resets number mode
                                               

      isNumberMode = false;
      result += " ";
    } else {
      let char;
      if (isNumberMode) {
        char = Object.keys(englishToBraille).find(
          
          (key) => englishToBraille[key] === brailleChar && !isNaN(key) // Translate the Braille character to a number
        );
      } else {
        char = brailleToEnglish[brailleChar]; // Translate the Braille character to a letter
      }

      if (char) {
        result += char;
      }
    }

    i += 6; // Move to the next Braille character
  }

  return result;
};

const input = process.argv.slice(2).join(" ");
console.log(translate(input));
