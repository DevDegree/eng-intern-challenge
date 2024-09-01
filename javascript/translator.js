const lettersSymbols = {
  A: "O.....",
  B: "O.O...",
  C: "OO....",
  D: "OO.O..",
  E: "O..O..",
  F: "OOO...",
  G: "OOOO..",
  H: "O.OO..",
  I: ".OO...",
  J: ".OOO..",
  K: "O...O.",
  L: "O.O.O.",
  M: "OO..O.",
  N: "OO.OO.",
  O: "O..OO.",
  P: "OOO.O.",
  Q: "OOOOO.",
  R: "O.OOO.",
  S: ".OO.O.",
  T: ".OOOO.",
  U: "O...OO",
  V: "O.O.OO",
  W: ".OOO.O",
  X: "OO..OO",
  Y: "OO.OOO",
  Z: "O..OOO",
  ".": "..O.O",
  ",": "..O...",
  "?": "..O.O",
  "!": "..O.",
  ":": "..O..",
  ";": "..O.O.",
  "-": "....O",
  "/": ".O..O.",
  "<": ".O..O",
  ">": "O..O.",
  "(": "O.O..O",
  ")": ".O.O.",
  " ": "......",
};

const nums = {
  1: lettersSymbols["A"],
  2: lettersSymbols["B"],
  3: lettersSymbols["C"],
  4: lettersSymbols["D"],
  5: lettersSymbols["E"],
  6: lettersSymbols["F"],
  7: lettersSymbols["G"],
  8: lettersSymbols["H"],
  9: lettersSymbols["I"],
  0: lettersSymbols["J"],
};

const capitalFollows = ".....O";
const numberFollows = ".O.OOO";
const decimalFollows = ".O...O";

const letterSymbolsKeys = Object.keys(lettersSymbols);
const numberKeys = Object.keys(nums);
const capitalLetters = letterSymbolsKeys.slice(0, 25);

function translate(message) {
  // check if message is in braille
  let translation;
  if (message.includes("..") || message.includes("OO")) {
    translation = decode(message);
  } else {
    translation = encode(message);
  }
  return translation;
}

function encode(string) {
  const encodedString = [];

  const stringChars = string.split("");

  stringChars.map((char, index) => {
    if (numberKeys.includes(char)) {
      // first number adds numberFollows along with encoded number
      const previousChar = stringChars[index - 1];
      if (index === 0 || !numberKeys.includes(previousChar)) {
        encodedString.push(numberFollows);
      }
      const encodedNumber = nums[char];
      encodedString.push(encodedNumber);
    } else {
      const nextChar = stringChars[index + 1];
      if (char === "." && numberKeys.includes(nextChar)) {
        encodedString.push(decimalFollows);
      } else {
        if (capitalLetters.includes(char)) {
          encodedString.push(capitalFollows);
        }
        const encodedChar = lettersSymbols[char.toUpperCase()];
        encodedString.push(encodedChar);
      }
    }
  });
  return encodedString.join("");
}

function decode(string) {
  const decodedString = [];
  // separate string in substrings of 6 characters
  const encodedChars = [];
  for (let i = 0; i < string.length; i += 6) {
    encodedChars.push(string.substring(i, i + 6));
  }
  let numberDecode = false;
  let capitalize = false;
  encodedChars.map((encodedChar) => {
    if (encodedChar === numberFollows) {
      numberDecode = true;
      return;
    }
    if (numberDecode) {
      if (encodedChar === "......") {
        decodedString.push(" ");
        numberDecode = false;
      } else {
        const decodedChar = getKeyByValue(nums, encodedChar);
        decodedString.push(decodedChar);
      }
    } else {
      if (encodedChar === capitalFollows) {
        capitalize = true;
        return;
      }
      const decodedChar = getKeyByValue(lettersSymbols, encodedChar);
      capitalize ? decodedString.push(decodedChar) : decodedString.push(decodedChar.toLowerCase());
      capitalize = false;
    }
  });
  return decodedString.join("");
}

function getKeyByValue(object, value) {
  return Object.keys(object).find((key) => object[key] === value);
}

const userInput = String(process.argv.slice(2).join(" "));
console.log(translate(userInput));
