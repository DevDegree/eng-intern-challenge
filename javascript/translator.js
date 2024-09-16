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
  n: "OOO.O.",
  o: "O..OO.",
  p: "OO.OO.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OOO.OO",
  z: "O..OOO",
  capitalfollows: ".....O",
  numberfollows: ".O.OOO",
  " ": "......",
};

const brailleNumberMap = {
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

const englishMap = Object.fromEntries(
  Object.entries(brailleMap).map(([key, value]) => [value, key])
);

const englishNumberMap = Object.fromEntries(
  Object.entries(brailleNumberMap).map(([key, value]) => [value, key])
);

function isBraille(str) {
  const brailleChars = new Set(["O", "."]);
  return (
    [...str].every((char) => brailleChars.has(char)) && str.length % 6 === 0
  );
}

function translateBrailleToEnglish(str) {
  var translated = "";
  var isCapital = false;
  var isNumber = false;

  for (let i = 0; i < str.length; i += 6) {
    const brailleChar = str.slice(i, i + 6);

    if (brailleChar === brailleMap.numberfollows) {
      isNumber = true;
      continue;
    }
    if (brailleChar === brailleMap.capitalfollows) {
      isCapital = true;
      continue;
    }
    if (brailleChar === brailleMap["......"]) {
      isNumber = false;
      translated += " ";
      continue;
    }

    let englishChar = isNumber
      ? englishNumberMap[brailleChar]
      : englishMap[brailleChar];

    translated += isCapital ? englishChar.toUpperCase() : englishChar;

    isCapital = false;
  }
  return translated;
}

function translateEnglishtoBraille(str) {
  let translated = "";
  let inNumber = false;

  for (const char of str) {
    if (char >= "0" && char <= "9") {
      if (!inNumber) {
        translated += brailleMap.numberfollows;
        inNumber = true;
      }
      translated += brailleNumberMap[char];
      continue;
    }

    if (inNumber && char === " ") {
      translated += brailleMap[" "];
      inNumber = false;
      continue;
    }

    if (char >= "A" && char <= "Z") {
      translated += brailleMap.capitalfollows + brailleMap[char.toLowerCase()];
      continue;
    }
    translated += brailleMap[char];
  }
  return translated;
}

function translate(str) {
  if (isValid(str)) {
    if (isBraille(str)) {
      return translateBrailleToEnglish(str);
    } else {
      return translateEnglishtoBraille(str);
    }
  } else {
    console.error("Only letters, numbers, and spaces can be inputted");
  }
}

function isValid(str) {
  const validPattern = /^[A-Za-z0-9 .]+$/;
  return validPattern.test(str);
}

const str = process.argv.slice(2).join(" ");
console.log(translate(str));
