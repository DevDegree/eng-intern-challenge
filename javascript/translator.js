// English to Braille characters
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
  " ": "......",
};

// Special Braille symbols
const brailleSpecials = {
  capital: ".....O", // next capital
  number: ".O.OOO", // next numver
};

// function to reverse key-value pairs  to decode Braille to English
const reverseMapping = (obj) => {
  const reversed = {};
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      reversed[obj[key]] = key;
    }
  }
  return reversed;
};
//Braille back to English
const reverseAlphabet = reverseMapping(brailleAlphabet);

// Mappings between numbers and letters a-j
const numberToLetter = {
  1: "a",
  2: "b",
  3: "c",
  4: "d",
  5: "e",
  6: "f",
  7: "g",
  8: "h",
  9: "i",
  0: "j",
};

const letterToNumber = {
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

//  English to Braille
const translateToBraille = (input) => {
  let braille = "";
  let numberMode = false; //track if we are in number mode

  for (const char of input) {
    if (char.match(/[A-Z]/)) {
      // If  uppercase, add symbol and convert to lowercase
      braille += brailleSpecials.capital + brailleAlphabet[char.toLowerCase()];
      numberMode = false;
    } else if (char.match(/[0-9]/)) {
      // If number, activate number mode and add the number follows symbol
      if (!numberMode) {
        braille += brailleSpecials.number;
        numberMode = true;
      }
      const letter = numberToLetter[char];
      braille += brailleAlphabet[letter];
    } else if (char === " ") {
      // add space
      braille += brailleAlphabet[" "];
      numberMode = false; // reset number mode
    } else if (char.match(/[a-z]/)) {
      // for all other characters
      braille += brailleAlphabet[char];
      numberMode = false;
    }
  }
  return braille;
};

//  Braille to English
const translateToEnglish = (braille) => {
  let english = "";
  let numberMode = false;
  let capitalizeNext = false;

  // 6 is the length of each Braille symbol
  const symbols = braille.match(/.{6}/g);

  for (const symbol of symbols) {
    // check if capital
    if (symbol === brailleSpecials.capital) {
      capitalizeNext = true;
      // check if number
    } else if (symbol === brailleSpecials.number) {
      numberMode = true;
      // if space
    } else if (symbol === brailleAlphabet[" "]) {
      english += " ";
      numberMode = false;
    } else {
      const char = reverseAlphabet[symbol];
      if (char) {
        if (numberMode) {
          const num = letterToNumber[char];
          if (num) {
            english += num;
          }
        } else {
          if (capitalizeNext) {
            english += char.toUpperCase();
            capitalizeNext = false; // Reset capitalization flag after use
          } else {
            english += char;
          }
        }
      }
    }
  }
  return english;
};

// Main function
const main = () => {
  const args = process.argv.slice(2);
  const input = args.join(" ");

  // Remove spaces for detection
  const inputNoSpaces = input.replace(/ /g, "");

  // input is Braille or English
  if (/^[O.]+$/.test(inputNoSpaces)) {
    console.log(translateToEnglish(input));
  } else {
    console.log(translateToBraille(input));
  }
};

main();
