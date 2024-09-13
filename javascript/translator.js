const brailleDict = {
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
  ";": "..O.O.",
  "-": "....OO",
  "!": "..OOO.",
  "?": "..O.OO",
  "(": "O.O..O",
  ")": ".O.OO.",
  DECIMAL: ".O...O",
  NUMBER: ".O.OOO",
  CAPITAL: ".....O",
};

const numberBrailleDict = {
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

const textDict = Object.fromEntries(
  Object.entries(brailleDict).map(([k, v]) => [v, k])
);
const numberDict = Object.fromEntries(
  Object.entries(numberBrailleDict).map(([k, v]) => [v, k])
);

function textToBraille(text) {
  let result = "";
  let i = 0;
  while (i < text.length) {
    let char = text[i];

    if (char.match(/[0-9]/)) {
      result += brailleDict["NUMBER"];
      while (i < text.length) {
        char = text[i];
        let nextChar = text[i + 1] || "";

        if (char.match(/[0-9]/)) {
          result += numberBrailleDict[char];
        } else if (char === "." && nextChar.match(/[0-9]/)) {
          result += brailleDict["DECIMAL"];
        } else {
          break;
        }
        i++;
      }
    } else if (char.match(/[A-Z]/)) {
      result += brailleDict["CAPITAL"] + brailleDict[char.toLowerCase()];
      i++;
    } else if (char in brailleDict) {
      result += brailleDict[char];
      i++;
    } else {
      i++;
    }
  }
  return result;
}

function brailleToText(braille) {
  let result = "";
  let i = 0;
  while (i < braille.length) {
    const chunk = braille.slice(i, i + 6);

    if (chunk === brailleDict.CAPITAL) {
      const nextChunk = braille.slice(i + 6, i + 12);
      if (nextChunk in textDict) {
        result += textDict[nextChunk].toUpperCase();
        i += 12;
      } else {
        i += 6;
      }
    } else if (chunk === brailleDict.NUMBER) {
      i += 6;
      while (i < braille.length) {
        const numChunk = braille.slice(i, i + 6);
        if (numChunk in numberDict) {
          result += numberDict[numChunk];
          i += 6;
        } else if (numChunk === brailleDict.DECIMAL) {
          result += ".";
          i += 6;
        } else {
          break;
        }
      }
    } else if (chunk in textDict) {
      result += textDict[chunk];
      i += 6;
    } else {
      i += 6;
    }
  }
  return result;
}

function translate(input) {
  if (input.match(/^[O.]+$/)) {
    return brailleToText(input);
  } else {
    return textToBraille(input);
  }
}

const input = process.argv.slice(2).join(" ");
if (input) {
  console.log(translate(input));
}
