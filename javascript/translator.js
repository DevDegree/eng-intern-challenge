// braille
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
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
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

//english
const englishDictionary = {
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

//Engligh to Braille
function translateToBraille(string) {
  let resultArray = Array.from(string);
  let result = [];
  let isNumber = false;

  resultArray.forEach((char) => {
    // Check if character is a digit
    if (char >= "0" && char <= "9") {
      if (isNumber) {
         // If it's consecutive numbers, add only the Braille representation
        result.push(brailleDictionary[char]);
      } else {
        // If it's the first number, add the number indicator before the digit
        result.push(brailleDictionary["number"], brailleDictionary[char]);
        isNumber = true; 
      }
    } else if (char === ' ') {
      // handle space character
      isNumber = false;
      result.push(brailleDictionary["space"]);
    } else if (char.toUpperCase() === char) {
      // Handle capital letter
      result.push(brailleDictionary["capital"], brailleDictionary[char.toLowerCase()]);
      isNumber = false; // Reset isNumber for letters
    } else {
      // For lowercase letters, directly add Braille representation
      result.push(brailleDictionary[char]);
      isNumber = false; // Reset isNumber for letters
    }
  });
  return result.join("");
}


//Braille to Engligh
function translateToEnglish(string){
  let englishArray =[];
  let result = [];
  let isNumberEng = false;
  let nextCapital = false;

// Split the Braille string into chunks of 6
  while(string){
    englishArray.push(string.slice(0,6));
    string = string.slice(6);
  }
  englishArray.forEach((char) => {
    if(char === ".0.000") {
      //is its a number
      isNumberEng = true;
    } else if(char === "......") {
      // if its a space
      isNumberEng = false;
      result.push(englishDictionary[char]);
    } else if(nextCapital === true) {
      // if the next character shoud be capitalized
      result.push(englishDictionary[char].toUpperCase());
      nextCapital = false; //reset
    } else if (char === ".....O") {
      //if its capitalized 
      nextCapital = true;
    } else {
      //translate from braille to english
      result.push(englishDictionary[char])
    }

  })
  //return as string
  return result.join("");
}

//main translate function
function translate(string) {
  const regExp = /[A-Za-z]/;
  if(regExp.test(string)) {
    return translateToBraille(string);
  } else {
    return translateToEnglish(string);
  }
}
//get input
const input = process.argv.slice(2).join(" ");

if (input) {
  //print the result
  console.log(translate(input));
}

module.exports = translate;