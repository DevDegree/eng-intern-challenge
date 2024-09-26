// declare the braille dictionary keys and values
const brailleDictionary = {
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
  0: ".OOO..",
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

// declare the english letters dictionary keys and values
const englishLetterDictionary = {
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
  ".....O": "capital",
  "......": " ",
};

// declare the numbers dictionary
const numberDictionary = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

// create Braille translation function
function toBraille(string) {
  let newArray = Array.from(string);
  let results = [];
  let prevIsNumber = false;

  newArray.forEach((character) => {
    // check if character is a number
    if (character >= "0" && character <= "9") {
      if (prevIsNumber) {
        results.push(brailleDictionary[character]);
      } else {
        results.push(brailleDictionary["number"], brailleDictionary[character]);
        prevIsNumber = true;
      }
    }
    // check if character is a space and set prevIsNumber to false
    else if (character === " ") {
      prevIsNumber = false;
      results.push(brailleDictionary["space"]);
    }
    // check if character is upper case and handle
    else if (character.toUpperCase() === character) {
      results.push(
        brailleDictionary["capital"],
        brailleDictionary[character.toLowerCase()]
      );
    }
    // if no other conditions are met, regular letter
    else {
      results.push(brailleDictionary[character]);
    }
  });
  return results.join("");
}

// create English translation function
function toEnglish(string) {
  let newArray = [];
  let results = [];
  let isNumber = false;
  let nextCapital = false;

  // white string has value, push next 6 characters to array as a string, and update string to remove those characters
  while (string) {
    newArray.push(string.slice(0, 6));
    string = string.slice(6);
  }

  // loop through array
  newArray.forEach((character) => {
    // check if the Number to follow character is present and set isNumber to true if yes
    if (character === ".O.OOO") {
      isNumber = true;
    }
    // check if the character is a space, if yes, set isNumber to false and push space
    else if (character === "......") {
      isNumber = false;
      results.push(englishLetterDictionary[character]);
    }
    // check if number and push from number dictionary
    else if (isNumber) {
      results.push(numberDictionary[character]);
    }
    // check if next character is capital is true, and push capital character, reset nextCapital back to false
    else if (nextCapital === true) {
      results.push(englishLetterDictionary[character].toUpperCase());
      nextCapital = false;
    }
    // check if next character is to be a capital and set nextCapital to true;
    else if (character === ".....O") {
      nextCapital = true;
    }
    // if no other conditions are met, push regular character
    else {
      results.push(englishLetterDictionary[character]);
    }
  });

  // return the array as a string
  return results.join("");
}

// create called function to determine input string language
// and translate

function translate(string) {
  const regExp = /[A-NP-Za-z]/;
  if (regExp.test(string)) {
    return toBraille(string);
  } else {
    return toEnglish(string);
  }
}

const input = process.argv.slice(2).join(" ");

if (input) {
  console.log(translate(input));
}

module.exports = translate;
