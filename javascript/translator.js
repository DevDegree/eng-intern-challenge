const brailleMap = {
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
  ".": "..OO.O",
  ",": "..O...",
  "?": "...OOO",
  "!": "..OOO.",
  ":": "..OO..",
  "-": "..OO..",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  capital: ".....O",
  number: ".O.OOO",
};

const numberMap = {
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

function translateToBraille(input) {
  let brailleTranslation = "";
  let isPreviousCapital = false;
  let isNumberSequence = false;

  for (const char of input) {
    const lowerChar = char.toLowerCase();

    if (char !== lowerChar) {
      brailleTranslation += brailleMap["capital"];
      isPreviousCapital = true;
    } else {
      isPreviousCapital = false;
    }

    if (!isNaN(char) && char !== " ") {
      if (!isNumberSequence) {
        brailleTranslation += brailleMap["number"];
        isNumberSequence = true;
      }

      brailleTranslation += numberMap[char];
    } else {
      isNumberSequence = false;
      if (brailleMap[lowerChar] !== undefined) {
        brailleTranslation += brailleMap[lowerChar];
      }
    }
  }

  return brailleTranslation;
}

const reverseBrailleMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);

const reverseNumberMap = Object.fromEntries(
  Object.entries(numberMap).map(([key, value]) => [value, key])
);

function translateBrailleToEnglish(brailleInput) {
  let englishTranslation = "";
  let i = 0;
  let isNumberMode = false;

  while (i < brailleInput.length) {
    const brailleChar = brailleInput.substring(i, i + 6);

    if (brailleChar === brailleMap["capital"]) {
      i += 6;

      if (i + 6 <= brailleInput.length) {
        const nextChar = brailleInput.substring(i, i + 6);
        if (reverseBrailleMap[nextChar]) {
          englishTranslation += reverseBrailleMap[nextChar].toUpperCase();
          i += 6;
        }
      }
      continue;
    }

    if (brailleChar === brailleMap["number"]) {
      isNumberMode = true;
      i += 6;
      continue;
    }

    let translatedChar;
    if (isNumberMode) {
      translatedChar = reverseNumberMap[brailleChar]; //
      if (translatedChar) {
        englishTranslation += translatedChar;
      }
    } else {
      translatedChar = reverseBrailleMap[brailleChar];
      if (translatedChar) {
        englishTranslation += translatedChar;
      }
    }

    if (isNumberMode && translatedChar && !reverseNumberMap[brailleChar]) {
      isNumberMode = false;
    }

    i += 6;
  }

  return englishTranslation;
}

function handleInput(input) {
  const isBraille = /^[O.]+$/.test(input) && input.length % 6 === 0;

  if (isBraille) {
    return translateBrailleToEnglish(input);
  } else {
    return translateToBraille(input);
  }
}

const input = process.argv.slice(2).join(" ");
console.log(handleInput(input));
