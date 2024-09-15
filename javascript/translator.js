// mapping of English characters and special symbols to Braille
const brailleDictionary = {
  // all letters
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

  // all numbers
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

  // Special characters
  " ": "......", // space
  capital: ".....O", // capital letter prefix
  number: ".O.OOO", // number prefix
};

// Create a reverse mapping from Braille to English characters for easy lookup
const reverseBrailleDictionary = Object.fromEntries(
  Object.entries(brailleDictionary).map(([key, value]) => [value, key])
);

const translateBrailleToEnglish = (braille) => {
  const tokens = braille.match(/.{1,6}/g); // Split Braille input into chunks of 6 characters
  let result = "";
  let isNumber = false; // track if the current mode is number mode

  tokens.forEach((token, index) => {
    if (token === brailleDictionary["number"]) {
      // switch to number mode when the number prefix is detected
      isNumber = true;
    } else if (token === brailleDictionary["capital"]) {
      // a capital prefix is detected, capitalize the next character
      const nextToken = tokens[index + 1];
      if (nextToken) {
        result += reverseBrailleDictionary[nextToken].toUpperCase();
        tokens.splice(index + 1, 1); // remove the next token after processing it
      }
    } else if (token === brailleDictionary[" "]) {
      // add a space to the result when the space Braille pattern is detected
      result += " ";
      isNumber = false; // reset number mode after a space
    } else {
      // transalate current Braille token to English
      if (isNumber && /^[O.]+$/.test(token)) {
        // if in number mode, convert the token to a number
        result += Object.keys(brailleDictionary).find(
          (key) => brailleDictionary[key] === token && /[0-9]/.test(key)
        );
      } else {
        // regilar translation for letters and other characters
        result += reverseBrailleDictionary[token] || "";
        // exit number mode if the current token is not a number
        if (isNumber && !/[0-9]/.test(reverseBrailleDictionary[token])) {
          isNumber = false;
        }
      }
    }
  });

  return result;
};

const translateEnglishToBraille = (english) => {
  let result = "";
  let isNumber = false; // to track if the current mode is number mode

  for (const char of english) {
    if (/[A-Z]/.test(char)) {
      // if the character is uppercase, add a capital prefix and convert to lowercase Braille
      result +=
        brailleDictionary["capital"] + brailleDictionary[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      // if the character is a digit, add a number prefix if not already in number mode
      if (!isNumber) {
        result += brailleDictionary["number"];
        isNumber = true; // set flag to remain in number mode
      }
      result += brailleDictionary[char]; // append the Braille representation of the number
    } else {
      // Translate regular characters including spaces
      result += brailleDictionary[char] || "......"; // default to space for any unknown character
      isNumber = false; // exit number mode after any non-number character
    }
  }

  return result; // return the fully translated Braille string
};

// function to determine if the input is Braille or English and translate accordingly.
const translate = () => {
  const input = process.argv[2]; // get the input string from command line arguments

  // determine if the input is Braille (consisting of only 'O' and '.') or English
  if (/^[O.]+$/.test(input)) {
    console.log(translateBrailleToEnglish(input)); // translate from Braille to English
  } else {
    console.log(translateEnglishToBraille(input)); // translate from English to Braille
  }
};

translate();
