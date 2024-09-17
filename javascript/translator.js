// mapping letters to their corresponding Braille patterns
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
};

// Braille patterns for numbers 0-9
const brailleNumbers = {
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

// Braille patterns for special characters
const specialBraille = {
  capital: ".....O",
  number: ".O.OOO",
  space: "......",
};

// create reverse mappings for Braille to English
const englishAlphabet = {};
for (const [char, braille] of Object.entries(brailleAlphabet)) {
  englishAlphabet[braille] = char;
}

const englishNumbers = {};
for (const [num, braille] of Object.entries(brailleNumbers)) {
  englishNumbers[braille] = num;
}

// determine if the input is Braille
const isBraille = (input) => {
  const cleanedInput = input.replace(/\s+/g, "");
  return /^[O.]+$/.test(cleanedInput);
};

// translate English to Braille
const translateEnglishToBraille = (text) => {
  let brailleText = "";
  let numberMode = false;

  for (let i = 0; i < text.length; i++) {
    const char = text[i];

    if (char === " ") {
      brailleText += specialBraille["space"];
      numberMode = false;
      continue;
    }

    if (char >= "A" && char <= "Z") {
      brailleText += specialBraille["capital"];
      brailleText += brailleAlphabet[char.toLowerCase()] || "......";
      numberMode = false;
      continue;
    }

    if (char >= "0" && char <= "9") {
      if (!numberMode) {
        brailleText += specialBraille["number"];
        numberMode = true;
      }
      brailleText += brailleNumbers[char];
      continue;
    }

    if (char >= "a" && char <= "z") {
      brailleText += brailleAlphabet[char] || "......";
      numberMode = false;
      continue;
    }

    // handle other chars as spaces or ignore them
    brailleText += specialBraille["space"];
    numberMode = false;
  }

  return brailleText;
};

// translate Braille to English text
const translateBrailleToEnglish = (brailleText) => {
  let englishText = "";
  let isCapital = false;
  let numberMode = false;

  const brailleChars = brailleText.replace(/\s+/g, "").match(/.{1,6}/g) || [];

  for (const brailleChar of brailleChars) {
    if (brailleChar === specialBraille["space"]) {
      englishText += " ";
      numberMode = false;
      continue;
    }

    if (brailleChar === specialBraille["capital"]) {
      isCapital = true;
      continue;
    }

    if (brailleChar === specialBraille["number"]) {
      numberMode = true;
      continue;
    }

    let char = "";
    if (numberMode) {
      char = englishNumbers[brailleChar] || "";
    } else {
      char = englishAlphabet[brailleChar] || "";
    }

    if (isCapital && char) {
      char = char.toUpperCase();
      isCapital = false;
    }

    englishText += char;
  }

  return englishText;
};

// main translation function
const brailleTranslator = (input) => {
  if (isBraille(input)) {
    return translateBrailleToEnglish(input);
  } else {
    return translateEnglishToBraille(input);
  }
};

// get input from command-line arguments
const input = process.argv.slice(2).join(" ");

// perform translation and output the result
const output = brailleTranslator(input);
console.log(output);
