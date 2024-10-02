// Braille <> English
const brailleAlpha = {
  // lowercase alphabets
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
  // Numbers - same as letter a-j
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
  // Punctuation marks
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
  ")": ".O.OO.",
  " ": "......", // space
};

// Instructional symbols
const capFollows = ".....O";
const decimalFollows = ".O...O";
const numberFollows = ".O.OOO";

// English <> Braille
const englishAlpha = Object.fromEntries(
    Object.entries(brailleAlpha).map(
        ([key, value]) => [value, key]
    )
);

// Main section

// Translate English to Braille
function translateToBraille(text) {
  let resultBraille = "";
  let isNumber = false; // prepare for number translation

  for (let index = 0; index < text.length; index++) {
    const char = text[index];

    // Check if the character is an uppercase letter
    if (/[A-Z]/.test(char)) {
      // add the cap follows indicator to the result
      resultBraille += capFollows + brailleAlpha[char.toLowerCase()]; // Include capitalization
      isNumber = false;
    }

    // Convert lowercase letters
    else if (/[a-z]/.test(char)) {
      // Handle lowercase letters
      resultBraille += brailleAlpha[char];
      isNumber = false;
    }

    // Check if the charater is a number
    else if (/\d/.test(char)) {
      if (isNumber === false) {
        // add the indicator
        resultBraille += numberFollows;
        isNumber = true;
      }
      resultBraille += brailleAlpha[char];
    }

    // Convert decimals - differentiate from period
    else if (char === ".") {
      const prevChar = text[index - 1];
      const nextChar = text[index + 1];

      // decimal point appears between two digits
      if (/\d/.test(prevChar) && /\d/.test(nextChar)) {
        resultBraille += decimalFollows; // add indicator
      } else {
        // period (punctuation mark)
        resultBraille += brailleAlpha[char];
      }
      isNumber = false;
    }

    // Convert other characters in the alphabet
    else if (brailleAlpha[char]) {
      // Handle punctuation marks and other characters
      resultBraille += brailleAlpha[char];
      isNumber = false;
    }

    // Other unexpected characters
    else {
      console.error(`Unexpected character: '${char}'`);
      isNumber = false;
    }
  }
  return resultBraille;
}


// Convert Braille to English
function translateToEnglish(text) {
  let resultEnglish = "";
  let isNumber = false;

  // Split the braille string - 6 as one character
  const brailleChars = text.split(/.{1,6}/g) || [];


  for (let char of brailleChars) {
      // Check if the character is an uppercase letter
      if (char === capFollows) {
        // Skip the capitalization indicator and continue to next iteration
        isNumber = false;
        continue;
      }

      // Check if the character is a number
      else if (char == numberFollows) {
        isNumber = true;
        continue;
      }

      // Check if we have a decimal point
      else if (char === decimalFollows) {
        resultEnglish += "."; // Add decimal point to the result
        // isNumber = true;
        continue;
      }

      // Convert other existing characters in the Braille alphbet
      else if (englishAlpha[char]) {
        // get the corresponding character
        const convertedChar = englishAlpha[char];

        // check if the character should be treated as a number
        if (isNumber && /\d/.test(convertedChar)) {
          resultEnglish += convertedChar;
        } 
        // for cases where the string contains both number and letters
        else if (isNumber && /[a-z]/.test(convertedChar)) {
          resultEnglish += convertedChar;
        }

      // Convert other existing characters accordingly
      else {
        resultEnglish += convertedChar;
      }
      isNumber = false;
  }
      else {
        console.error(`Unexpected Braille character: '${char}'`);
        isNumber = false;
      }
    }

    return resultEnglish;
  }


// Test
// Braille to English
const engText = "Hello!"
const brailleResult = translateToBraille(engText);
console.log(brailleResult);

// English to Braille
const brailleText = ".....O.OO..O..O..O.O.O.O.O.O.O..OO...OOO."
const englishResult = translateToEnglish(brailleText);
console.log(englishResult)