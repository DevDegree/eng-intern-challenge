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
  A: ".....OO.....",
  B: ".....OO.O...",
  C: ".....OOO....",
  D: ".....OOO.O..",
  E: ".....OO..O..",
  F: ".....OOOO...",
  G: ".....OOOOO..",
  H: ".....OO.OO..",
  I: ".....O.OO...",
  J: ".....O.OOO..",
  K: ".....OO...O.",
  L: ".....OO.O.O.",
  M: ".....OOO..O.",
  N: ".....OOO.OO.",
  O: ".....OO..OO.",
  P: ".....OOOO.O.",
  Q: ".....OOOOOO.",
  R: ".....OO.OOO.",
  S: ".....O.OO.O.",
  T: ".....O.OOOO.",
  U: ".....OO...OO",
  V: ".....OO.O.OO",
  W: ".....O.OOO.O",
  X: ".....OOO..OO",
  Y: ".....OOO.OOO",
  Z: ".....OO..OOO",
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
  " ": "......",
  ".": ".O.O..",
  ",": ".O....",
  ";": ".OO...",
  "-": "..OO..",
  "!": ".OOO..",
  "?": ".O..O.",
  "(": ".OOO.O",
  ")": ".OOOO.",
  DECIMAL: ".O...O",
  NUMBER: ".O.OOO",
};

const textDict = Object.fromEntries(
  Object.entries(brailleDict).map(([k, v]) => [v, k])
);

function textToBraille(text) {
  let result = "";
  let prevChar = "";
  let isNumberMode = false;

  for (let i = 0; i < text.length; i++) {
    let char = text[i];
    let nextChar = text[i + 1] || "";

    if (!char.match(/[0-9\s]/) && nextChar.match(/[0-9]/)) {
      result += brailleDict["NUMBER"];
      isNumberMode = true;
    } else if (char.match(/[0-9]/)) {
      if (!isNumberMode) {
        result += brailleDict["NUMBER"];
        isNumberMode = true;
      }
      result += brailleDict[char];
    } else {
      isNumberMode = false;
      if (char in brailleDict) {
        result += brailleDict[char];
      }
    }

    if (char === "." && prevChar.match(/[0-9]/) && nextChar.match(/[0-9]/)) {
      result += brailleDict["DECIMAL"];
    }

    prevChar = char;
  }

  return result;
}

function brailleToText(braille) {
  let result = "";
  let i = 0;

  while (i < braille.length) {
    let char = "";
    if (i + 12 <= braille.length && braille.slice(i, i + 12) in textDict) {
      char = textDict[braille.slice(i, i + 12)];
      i += 12;
    } else if (i + 6 <= braille.length && braille.slice(i, i + 6) in textDict) {
      char = textDict[braille.slice(i, i + 6)];
      i += 6;
    } else {
      i += 6;
    }
    result += char;
  }

  return result.replace(/DECIMAL/g, ".");
}

function translate(input) {
  if (input.match(/^[O.]+$/)) {
    return brailleToText(input);
  } else {
    return textToBraille(input);
  }
}

function runTest(input, expect) {
  const output = translate(input);
  console.log(`Input: ${input}`);
  console.log(`Output: ${output}`);
  console.log(`Expect: ${expect}`);
  console.log(`Test ${output === expect ? "PASSED" : "FAILED"}`);
  console.log("---");
}

runTest(
  "Hello world",
  ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
);
runTest("42", ".O.OOOOO.O..O.O...");
runTest("Abc 123", ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....");
runTest(
  "Abc 123 xYz",
  ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
);

const input = process.argv.slice(2).join(" ");
if (input) {
  console.log(translate(input));
}
