// Map of Braille to Characters
const brailleToChar = {
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
  ".....O": "capital follows",
  ".O.OOO": "number follows",
};

const charToBraille = Object.fromEntries(
  Object.entries(brailleToChar).map(([k, v]) => [v, k])
);

const charToNumbers = {
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

function convertBrailleToChar(brailleInput) {
  let result = "";
  let capitalNext = false;
  let numberMode = false;

  //   Loop through input string in groups of 6
  for (let i = 0; i < brailleInput.length; i += 6) {
    const brailleChar = brailleInput.slice(i, i + 6);
    if (char === "capital follows") {
      capitalNext = true;
    } else if (char === "number follows") {
      numberMode = true;
    } else if (char === " ") {
      result += " ";
      numberMode = false;
    } else if (numberMode) {
      result +=
        Object.keys(charToNumbers).find((key) => charToNumbers[key] === char) ||
        char;
    } else {
      result += capitalNext ? char.toUpperCase() : char;
      capitalNext = false;
    }
  }

  return result;
}

function convertCharToBraille(charInput) {
  let result = "";
  let numberMode = false;

  for (let i = 0; i < charInput.length; i++) {
    const char = charInput[i];
    if (char >= "0" && char <= "9") {
      if (!numberMode) {
        result += charToBraille["number follows"];
        numberMode = true;
      }
      result +=
        charToBraille[
          Object.keys(charToNumbers).find((key) => charToNumbers[key] === char)
        ];
    } else {
      if (numberMode && char !== " ") {
        result += charToBraille[" "];
      }
      numberMode = false;
      // checks if chracter is an uppercase character, if so adds indicator of capital follows
      if (char >= "A" && char <= "Z") {
        result +=
          charToBraille["capital follows"] + charToBraille[char.toLowerCase()];
      } else {
        result += charToBraille[char.toLowerCase()] || "Unknown Character";
      }
    }
  }

  return result;
}

function checkIfInputIsBraille(input) {
  return (
    // Checks to make sure only chracters O and . are being used
    input.split("").every((char) => char === "O" || char === ".") &&
    // check if length of input string is divisible by 6, as braille is map is divisible by 6
    input.length % 6 === 0
  );
}

function translateInput(inputString) {
  // Check if input string is in Brailler format, otherwise assume it is regular characters
  return checkIfInputIsBraille(inputString)
    ? convertBrailleToChar(inputString)
    : convertCharToBraille(inputString);
}

if (require.main === module) {
  const inputString = process.argv.slice(2).join(" ");
  // Check if input string is empty or undefined
  if (inputString === undefined || inputString === "") {
    console.log("Input a string to translate.");
  } else {
    const translatedString = translateInput(inputString);
    console.log(translatedString);
  }
}