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
  return translatedText;
}

function translateEnglishToBraille(english) {
  let translatedBraille = "";
  let isNumeric = false;

  // Loop through each character in the English input string
  for (let i = 0; i < english.length; i++) {
    // Current character
    const character = english[i];
    // Check if the character is a letter (case-insensitive)
    if (brailleAlphaMapping[character.toLowerCase()]) {
      //check if the letter is uppercase.
      if (
        character == character.toUpperCase() &&
        character !== character.toLowerCase()
      ) {
        translatedBraille += brailleSpecialMapping.capital;
      }
      // Append the corresponding Braille character for the letter
      translatedBraille += brailleAlphaMapping[character.toLowerCase()];
    } else if (brailleNumMapping[character]) {
      // Handle numeric characters
      if (!isNumeric) {
        translatedBraille += brailleSpecialMapping.number;
        isNumeric = true;
      }
      // Append the corresponding Braille character for the number
      translatedBraille += brailleNumMapping[character];
    } else if (character === " ") {
      // Handle spaces
      translatedBraille += brailleSpecialMapping.space;
      isNumeric = false; // Reset numeric flag after space
    }
  }
  return translatedBraille;
}

function main(inputArr) {
  // Throws error if no argument is provided.
  if (!inputArr) {
    console.log("Please provide a valid input - Braille or English");
  }
  // Join the array elements into a single string separated by spaces
  let text = inputArr.join(" ");
  let result;

  // Determine if the input text is Braille or English
  if (isBraille(text)) {
    result = translateBrailleToEnglish(text);
  } else {
    result = translateEnglishToBraille(text);
  }

  // Output the result to the console
  console.log(result);
}

// Calling the main function with command line arguments
var args = process.argv.slice(2);
main(args);
