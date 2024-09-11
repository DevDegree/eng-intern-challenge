const englishToBraille = {
  // letters
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

  //numbers
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

  //special
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

const brailleToEnglish = Object.fromEntries(
  Object.entries(englishToBraille)
    // exclude numbers from mapping
    .filter(([key]) => !key.match(/\d/))
    .map(([key, value]) => [value, key])
);

function englishToBrailleTranslation(input) {
  let result = "";
  let isNumber = false;

  for (let char of input) {
    if (char === " ") {
      result += englishToBraille["space"];
      //reset isNumber after space
      isNumber = false;
    } else if (!isNaN(char)) {
      if (!isNumber) {
        result += englishToBraille["number"];
        isNumber = true;
      }
      result += englishToBraille[char];
    } else {
      if (char === char.toUpperCase()) {
        result += englishToBraille["capital"];
      }
      let lowerCaseChar = char.toLowerCase();
      result += englishToBraille[lowerCaseChar];
      isNumber = false;
    }
  }
  return result;
}

function brailleToEnglishTranslation(input) {
  let result = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < input.length; i += 6) {
    let brailleSymbol = input.slice(i, i + 6);
    let engChar = brailleToEnglish[brailleSymbol];

    if (brailleSymbol === englishToBraille["space"]) {
      result += " ";
      isNumber = false;
      continue;
    }

    if (brailleSymbol === englishToBraille["capital"]) {
      isCapital = true;
      continue;
    }

    if (brailleSymbol === englishToBraille["number"]) {
      isNumber = true;
      continue;
    }

    if (!engChar) {
      return "Invalid Braille input";
    }

    if (isCapital) {
      engChar = engChar.toUpperCase();
      isCapital = false;
    }

    if (isNumber) {
      engChar = Object.keys(englishToBraille).find(
        (key) => englishToBraille[key] === brailleSymbol && key.match(/\d/)
      );
    }
    result += engChar;
  }
  return result;
}

//get input from terminal
const input = process.argv.slice(2).join(" ");

function isValidBrailleInput(input) {
  if (/^[O.]+$/.test(input)) {
    return input.length % 6 === 0;
  }
}

function isValidEnglishInput(input) {
  return /^[a-zA-Z0-9\s]+$/.test(input);
}

if (!input) {
  console.error("Empty input");
} else if (isValidBrailleInput(input)) {
  try {
    const translation = brailleToEnglishTranslation(input);
    console.log(translation);
  } catch (error) {
    console.error("Braille to English translation error");
  }
} else if (isValidEnglishInput(input)) {
  try {
    const translation = englishToBrailleTranslation(input);
    console.log(translation);
  } catch (error) {
    console.error("English to Braille translation error:");
  }
} else {
  console.error("Invalid input");
}
