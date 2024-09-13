const englishToBrailleDictionary = {
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

const numbersToBrailleDictionary = {
  0: ".OOO..",
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
};

const capitalizeNext = ".....O";

const numberNext = ".O.OOO";

const spaceNext = "......";

// reverse objects key and values to convert braille to alphabets & numbers

const brailleToEnglishDictionary = Object.entries(
  englishToBrailleDictionary
).reduce((accumulator, [key, value]) => {
  accumulator[value] = key;
  return accumulator;
}, {});

const brailleToNumbersDictionary = Object.entries(
  numbersToBrailleDictionary
).reduce((accumulator, [key, value]) => {
  accumulator[value] = key;
  return accumulator;
}, {});

// function to translate english alphabets & numbers to Braille
function englishToBrailleTranslator(input) {
  const arr = input.split("");

  let capitalSeries = false;
  let numberSeries = false;

  const converted = arr.map((letter) => {
    if (letter === " ") {
      return spaceNext;
    } else if (isNaN(letter) && letter === letter.toUpperCase()) {
      capitalSeries = true;
      return capitalizeNext + englishToBrailleDictionary[letter.toLowerCase()];
    } else if (letter >= "0" && letter <= "9") {
      if (numberSeries === false) {
        numberSeries = true;
        return numberNext + numbersToBrailleDictionary[letter];
      } else {
        return numbersToBrailleDictionary[letter];
      }
    } else {
      return englishToBrailleDictionary[letter];
    }
  });
  return converted.join("");
}

// function to translate Braille to english alphabets & numbers
function brailleToEnglishTranslator(input) {
  const brailleLetters = input.match(/.{1,6}/g);

  let isCapital = false;
  let isNumber = false;

  const converted = brailleLetters.map((sequence) => {
    if (sequence === spaceNext) {
      return " ";
    } else if (sequence === capitalizeNext) {
      isCapital = true;
      return "";
    } else if (sequence === numberNext) {
      isNumber = true;
      return "";
    } else {
      if (isNumber) {
        if (sequence === spaceNext) {
          isNumber = false;
        }
        return brailleToNumbersDictionary[sequence];
      } else {
        if (isCapital) {
          isCapital = false;
          return brailleToEnglishDictionary[sequence].toUpperCase();
        } else {
          return brailleToEnglishDictionary[sequence];
        }
      }
    }
  });
  return converted.join("");
}

// translator function to check input language and convert it
function translator(input) {
  if (input.includes(".") && input.includes("O")) {
    console.log(brailleToEnglishTranslator(input));
  } else {
    console.log(englishToBrailleTranslator(input));
  }
}

// Read input from command line arguments
const input = process.argv.slice(2).join(" ");
translator(input);
