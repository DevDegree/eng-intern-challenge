// English to Braille mapping
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
  " ": "......", 
  cap: ".....O",
  num: ".O.OOO", 
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
};

// Braille to English mapping (reverse of the above)
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
  ".....O": "cap", 
  ".O.OOO": "num", 
};

(function main() {
    const input = process.argv.slice(2).join(' ');
    
    if (input) {
        if (isBraille(input)) {
        translateBrailleToEnglish(input);
        console.log(`${translateBrailleToEnglish(input)}`); 
        } else {
        translateEnglishToBraille(input);
        console.log(`${translateEnglishToBraille(input)}`); 
        }
    } else {
        console.log("Please provide an input string.");
    }
})();

// Function to determine whether input is Braille or English
function isBraille(input) {
    // check if input contains only "O" and "." and if its length is divisible by 6
    const isValidBraille = /^[O.]+$/.test(input) && input.length % 6 === 0;
    return isValidBraille;
  }

// Function to translate English to Braille
function translateEnglishToBraille(englishString) {
  let brailleTranslation = "";
  let isNumber = false; 

  for (let char of englishString) {
    const lowerChar = char.toLowerCase();
    
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        brailleTranslation += englishToBraille["num"];
        isNumber = true; // We are now in a number sequence
      }
      
      brailleTranslation += englishToBraille[char];
    } else {
      isNumber = false;


      if (char !== lowerChar && /[a-zA-Z]/.test(char)) {
        brailleTranslation += englishToBraille["cap"]; //  capitalization marker
      }

      if (englishToBraille[lowerChar]) {
        brailleTranslation += englishToBraille[lowerChar];
      } else {
        brailleTranslation += "?"; // handle unknown characters (just in case)
      }
    }
  }

  return brailleTranslation;
}

// Function to translate Braille to English
function translateBrailleToEnglish(brailleString) {
  let englishTranslation = "";
  let isCapital = false;
  let isNumber = false;

  // Loop through the Braille string in chunks of 6 characters
  for (let i = 0; i < brailleString.length; i += 6) {
    const brailleChar = brailleString.substring(i, i + 6);

    // check for the capitalization marker
    if (brailleChar === ".....O") {
      isCapital = true;
      continue; 
    }

    // check for the number marker
    if (brailleChar === ".O.OOO") {
      isNumber = true;
      continue; 
    } 

    let englishChar;
    if (brailleToEnglish[brailleChar]) {
      if (isNumber) {
        // Translate Braille number (Braille numbers are the same as a-j in Braille)
        const numberMap = {
          a: "1",
          b: "2",
          c: "3",
          d: "4",
          e: "5",
          f: "6",
          g: "7",
          h: "8",
          i: "9",
          j: "0",
        };
        englishChar = numberMap[brailleToEnglish[brailleChar]];
      } else {
        englishChar = brailleToEnglish[brailleChar];
      }

      if (isCapital && englishChar !== " ") {
        englishChar = englishChar.toUpperCase();
        isCapital = false; 
      }

 
      englishTranslation += englishChar;
    } else {
      englishTranslation += "?"; 
    }

    brailleString.substring(i+6, i + 12)

    // Reset the number flag if the next character is a space ie. number sequence has ended
    if (brailleString.substring(i+6, i + 12) == "......") {
      isNumber = false;
    }
  }

  return englishTranslation;
}
