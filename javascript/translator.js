const { createInterface } = require("readline");

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const brailleToEnglish = {
  "O.....": ["a", "1"],
  "O.O...": ["b", "2"],
  "OO....": ["c", "3"],
  "OO.O..": ["d", "4"],
  "O..O..": ["e", "5"],
  "OOO...": ["f", "6"],
  "OOOO..": ["g", "7"],
  "O.OO..": ["h", "8"],
  ".OO...": ["i", "9"],
  ".OOO..": ["j", "O"],
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
  "....OO": " ",
  ".....O": "capital follows",
  ".O...O": "decimal follows",
  ".O.OOO": "number follows",
  "..OO.O": ".",
  "..O...": ",",
  "..O.O.": ";",
  "..OO..": ":",
  "......": " ",
  "..O.OO": "?",
  "..OOO.": "!",
  "....OO": "-",
  "O.O..O": "(",
  ".O.OO.": ")",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..O.O": ">",
};

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
  O: ".OOO..",
  " ": "....OO",
  "capital follows": ".....O",
  "decimal follows": ".O...O",
  "number follows": ".O.OOO",
  ".": "..OO.O",
  ",": "..O...",
  ";": "..O.O.",
  ":": "..OO..",
  " ": "......",
  "?": "..O.OO",
  "!": "..OOO.",
  "-": "....OO",
  "(": "O.O..O",
  ")": ".O.OO.",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..O.O",
};

//Returns an array of strings with each string containing 6 characters
function splitEverySixChars(str) {
  return str.match(/.{1,6}/g);
}

rl.question("Enter a sentence: ", (inputString) => {
  let enteredValue = inputString;
  let seperatedCharacters = [];
  let translatedCharacters = [];
  let outputValue;
  let char;
  let isCapital = false;
  let isDecimal = false;
  let isNumber = false;

  //Ensure that Only Braille is inside the input string
  const isBraille = /^[.O]+$/;

  //If true then the input is Braille
  if (isBraille.test(enteredValue)) {
    //If the length Of the input is not divisible by 6 then it is not a valid Braille input
    if (enteredValue.length % 6 !== 0) {
      rl.close();
      return console.log(
        "Invalid Braille input sequence. Ensure that the input is a valid Braille sequence."
      );
    }

    //Slice the input string into an array where each index contains 6 characters
    seperatedCharacters = splitEverySixChars(enteredValue);

    //Iterate through the array and translate the Braille characters to English
    for (let i = 0; i < seperatedCharacters.length; i++) {
      char = seperatedCharacters[i];

      //If the Braille character is not in the Braille to English object then it is not a valid Braille pattern
      if (brailleToEnglish[char] === undefined) {
        rl.close();
        return console.log(
          "Invalid Braille pattern. Ensure that the input is a valid Braille pattern. "
        );
      }

      if (brailleToEnglish[char] === "capital follows") {
        isCapital = true;
        continue;
      }

      if (brailleToEnglish[char] === "decimal follows") {
        isDecimal = true;
        continue;
      }

      if (brailleToEnglish[char] === "number follows") {
        isNumber = true;
        continue;
      }

      if (brailleToEnglish[char] === " ") {
        isNumber = false;
        translatedCharacters.push(brailleToEnglish[char]);
        continue;
      }

      if (isCapital) {
        translatedCharacters.push(brailleToEnglish[char][0].toUpperCase());
        isCapital = false;
        continue;
      }

      if (isDecimal) {
        translatedCharacters.push(brailleToEnglish[char]);
        isDecimal = false;
        continue;
      }

      if (isNumber) {
        translatedCharacters.push(brailleToEnglish[char][1]);
        continue;
      }

      if (brailleToEnglish[char].length === 2) {
        translatedCharacters.push(brailleToEnglish[char][0]);
      } else {
        translatedCharacters.push(brailleToEnglish[char]);
      }
    }

    //Join the translated characters into a string
    outputValue = translatedCharacters.join("");
    console.log(outputValue);
    rl.close();
  } else {
    //If false then the input is English

    //Split the input string into an array of characters
    seperatedCharacters = enteredValue.split("");

    for (let i = 0; i < enteredValue.length; i++) {
      char = seperatedCharacters[i];

      if (char === " ") {
        isNumber = false;
        translatedCharacters.push(englishToBraille[char]);
        continue;
      }

      if (isNumber) {
        if (char === ".") {
          translatedCharacters.push(englishToBraille["decimal follows"]);
          translatedCharacters.push(englishToBraille[char]);
          continue;
        }
      }

      //Check if the character is a number
      if (Number(char)) {
        isNumber = true;
        translatedCharacters.push(englishToBraille["number follows"]);
        translatedCharacters.push(englishToBraille[char]);
        continue;
      }

      if (char === char.toUpperCase()) {
        translatedCharacters.push(englishToBraille["capital follows"]);
        translatedCharacters.push(englishToBraille[char.toLowerCase()]);
        continue;
      }

      if (char === char.toLowerCase()) {
        translatedCharacters.push(englishToBraille[char]);
      }
    }

    //Join the translated characters into a string
    outputValue = translatedCharacters.join("");
    console.log(outputValue);
    rl.close();
  }
});
