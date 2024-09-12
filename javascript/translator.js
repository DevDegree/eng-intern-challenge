// Because the symbol ">" and the letter "o" have the same pattern in Braille, the ">" and "<" are assumed to be used to compare numbers only. It is assuemd those operators are in between numbers and there are no spaces between the numbers and the operators.

// VARIABLES
const engToBraille = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  ";": "..O.O.",
  "-": "....OO",
  "/": ".O..O.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const brailleToEng = inverse(engToBraille);

const engToBrailleNums = {
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
  "<": ".OO..O",
  ">": "O..OO.",
};

const brailleToEngNums = inverse(engToBrailleNums);

const capitalSign = ".....O";
const decimalSign = ".O...O";
const numberSign = ".O.OOO";
const spaceSign = "......";
let resultString = "";
let isCapital = false;
let isNumber = false;
let isDecimal = false;
let brStrings = [];

const userInput = process.argv.slice(2).join(" ");

// Checks to see if Braille or English then proceeds to translate
if (isBraille(userInput)) {
  for (let i = 0; i < userInput.length; i += 6) {
    brStrings.push(userInput.substring(i, i + 6));
  }

  for (const cluster of brStrings) {
    if (cluster === spaceSign) {
      isNumber = false;
    }
    if (
      cluster === capitalSign ||
      cluster === decimalSign ||
      cluster === numberSign
    ) {
      switch (cluster) {
        case capitalSign:
          isCapital = true;
          break;
        case decimalSign:
          isDecimal = true;
          break;
        case numberSign:
          isNumber = true;
          break;
        default:
          break;
      }
    } else {
      if (isCapital) {
        let capitalChar = brailleToEng[cluster];
        resultString += capitalChar.toUpperCase();
        isCapital = false;
      } else if (isNumber) {
        if (isDecimal) {
          resultString += brailleToEng[cluster];
          isDecimal = false;
        } else {
          resultString += brailleToEngNums[cluster];
        }
      } else {
        resultString += brailleToEng[cluster];
      }
    }
  }

  console.log(resultString);
} else {
  for (letter of userInput) {
    let capitalRegex = /^[A-Z]*$/;
    let digitRegex = /^[0-9><]*$/;

    if (letter === " ") {
      resultString += spaceSign;
      isNumber = false;
    } else if (isNumber) {
      if (letter === ".") {
        resultString += decimalSign;
      } else {
        resultString += engToBrailleNums[letter];
      }
    } else if (letter.match(capitalRegex)) {
      resultString += capitalSign;
      resultString += engToBraille[letter.toLowerCase()];
    } else if (letter.match(digitRegex)) {
      resultString += numberSign;
      resultString += engToBrailleNums[letter];
      isNumber = true;
    } else {
      resultString += engToBraille[letter];
    }
  }
  console.log(resultString);
}

// HELPER FUNCTIONS
// checks if string is Braille
// returns true/false
function isBraille(input) {
  const brailleRegex = /^[O.]+$/;
  return brailleRegex.test(input);
}

// inverse function to create reverse map of english-braille map
function inverse(obj) {
  const inverseObj = {};
  for (const entry in obj) {
    inverseObj[obj[entry]] = entry;
  }
  return inverseObj;
}
