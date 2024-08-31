const process = require("node:process");

var args = process.argv.slice(2);
const input = args[0];

function invert(object) {
  var invertedObject = {};
  for (var key in object) {
    invertedObject[object[key]] = key;
  }
  return invertedObject;
}

const brailleAlphaMapping = {
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
  //   ".": "..OO.O",
  //   ",": "..O...",
  //   "?": "..O.OO",
  //   "!": "..OOO.",
  //   ":": "..OO..",
  //   ";": "..O.O.",
  //   "-": "....OO",
  //   "/": ".O..O.",
  //   "<": ".OO..O",
  //   ">": "O..OO.",
  //   "(": "O.O..O",
  //   ")": ".O.OO.",
};
const brailleNumMapping = {
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

const brailleSpecialMapping = {
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

function isBraille(text) {
  // Regular expression to match Braille (only "O" and ".")
  const brailleRegex = /^[O.]+$/;
  return brailleRegex.test(text);
}
function translateBrailleToEnglish(braille) {
  const invertedBrailleAlphaMapping = invert(brailleAlphaMapping);
  const invertedBrailleNumMapping = invert(brailleNumMapping);
  const invertedBrailleSpecialMapping = invert(brailleSpecialMapping);

  let isNumeric = false;
  let isCapital = false;

  // Break up the braille input into segments of length 6 - representing each braille character.
  let brailleCharacterArr = [];
  for (let i = 0; i < braille.length; i = i + 6) {
    brailleCharacterArr.push(braille.slice(i, i + 6));
  }

  let translatedText = "";
  for (let brailleCharacter of brailleCharacterArr) {
    if (invertedBrailleSpecialMapping[brailleCharacter]) {
      const flag = invertedBrailleSpecialMapping[brailleCharacter];
      if (flag === "capital") {
        isCapital = true;
      } else if (flag === "number") {
        isNumeric = true;
      } else {
        // last case is a space
        translatedText += " ";
        isNumeric = false; // Reset isNumeric flag after processing
      }
    } else {
      if (isNumeric) {
        translatedText += invertedBrailleNumMapping[brailleCharacter] || ""; // If a braille character is not found in mapping, add empty string.
      } else {
        if (isCapital) {
          translatedText +=
            invertedBrailleAlphaMapping[brailleCharacter].toUpperCase();
          isCapital = false; // Reset isCapital flag after processing
        } else {
          translatedText += invertedBrailleAlphaMapping[brailleCharacter] || ""; // Undefined handling
        }
      }
    }
  }
  console.log(translatedText);
  return translatedText;
}

function translateEnglishToBraille(english) {}

// testing util function
translateBrailleToEnglish(
  ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
); // expect: Hello world
translateBrailleToEnglish(
  ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
); // expect: Abc 123
translateBrailleToEnglish(".O.OOOOO.O..O.O..."); // expect 42
