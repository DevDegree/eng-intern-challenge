// step 1: define alphabet and indicators for uppercase, spaces and numbers
// step 2: check input to determine wether english or braille
// step 3: translate input and handle uppercase, spaces and numbers
// step 4: return and log translated string

const brailleAlphabet = {
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
};

const brailleNumbers = {
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
};

const combinedBraille = { ...brailleAlphabet, ...brailleNumbers };

const brailleUppercaseIndicator = ".....O";
const brailleNumberIndicator = ".O.OOO";
const brailleSpaceIndicator = "......";

// test input for braille or english, set inputLang accordingly
const args = process.argv.slice(2);
const inputString = args.join(" ");
const inputLang = /^[O.]+$/.test(inputString) ? "braille" : "english";

const brailleToEnglish = (brailleString) => {
  let translationString = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < brailleString.length; i += 6) {
    let chunk = brailleString.slice(i, i + 6);

    // check for uppercase
    if (chunk === brailleUppercaseIndicator) {
      isCapital = true;
      continue;
    }

    // check for number
    if (chunk === brailleNumberIndicator) {
      isNumber = true;
      continue;
    }

    // check for space
    if (chunk === brailleSpaceIndicator) {
      translationString += " ";
      isNumber = false; // assume all following symbols are numbers until the next space symbol
      continue;
    }

    let letter;

    // construct string, check if number or letter
    if (isNumber) {
      letter = Object.keys(brailleNumbers).find(
        (key) => brailleNumbers[key] === chunk
      );
      if (letter) {
        translationString += letter;
        continue;
      }
    } else {
      letter = Object.keys(brailleAlphabet).find(
        (key) => brailleAlphabet[key] === chunk
      );
      if (letter) {
        translationString += isCapital
          ? letter.toUpperCase()
          : letter.toLowerCase();
        isCapital = false;
      } else {
        console.log("Invalid chunk");
      }
    }
  }

  console.log(translationString);
  return translationString;
};

const englishToBraille = (englishString) => {
  let translationString = "";
  let isNumber = false;

  for (let i = 0; i < englishString.length; i++) {
    let char = englishString[i];

    // check if char is uppercase
    if (char === char.toUpperCase() && /[A-Z]/.test(char)) {
      translationString += brailleUppercaseIndicator;
      char = char.toLowerCase(); // convert to lowerCase for lookup
    }

    // check if char is a num
    if (/[0-9]/.test(char)) {
      if (!isNumber) {
        translationString += brailleNumberIndicator;
        isNumber = true;
      }
      translationString += brailleNumbers[char];
      continue;
    } else {
      isNumber = false; // reset number mode after non-number character
    }

    // check for spaces
    if (char === " ") {
      translationString += brailleSpaceIndicator;
      continue;
    }

    let brailleSymbol = combinedBraille[char];

    if (brailleSymbol) {
      translationString += brailleSymbol;
    } else {
      console.log("Invalid character");
    }
  }

  console.log(translationString);
  return translationString;
};

inputLang == "braille"
  ? brailleToEnglish(inputString)
  : englishToBraille(inputString);