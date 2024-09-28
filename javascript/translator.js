const textToBraille = {
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
  isCapt: ".....O",
  isDeci: ".O...O",
  isNumb: ".O.OOO",
  " ": "......",
};

const numToBraille = {
  1: textToBraille.a,
  2: textToBraille.b,
  3: textToBraille.c,
  4: textToBraille.d,
  5: textToBraille.e,
  6: textToBraille.f,
  7: textToBraille.g,
  8: textToBraille.h,
  9: textToBraille.i,
  0: textToBraille.j,
};

const brailleToText = Object.fromEntries(
  Object.entries(textToBraille).map(([key, value]) => [value, key])
);

const brailleToNum = Object.fromEntries(
  Object.entries(numToBraille).map(([key, value]) => [value, key])
);

const args = process.argv.slice(2).join(" ");

function isBraille(str) {
  if (str.length % 6 !== 0) {
    return false;
  }

  return /^[O.]+$/.test(str);
}

function convertToBraille(text) {
  let brailleText = "";
  isNum = false;

  for (let i = 0; i < text.length; i++) {
    if (text[i] >= "0" && text[i] <= "9") {
      //if char is number
      if (!isNum) {
        let numPrefix = textToBraille["isNumb"];
        brailleText += numPrefix + numToBraille[text[i]];
        isNum = true;
      } else {
        brailleText += numToBraille[text[i]];
      }
    } else {
      //if char is letter
      isNum = false;
      //check uppercase of alpha character
      if (text[i].match(/^[a-z]+$/i) && text[i] == text[i].toUpperCase()) {
        let uppPrefix = textToBraille["isCapt"];
        brailleText += uppPrefix + textToBraille[text[i].toLowerCase()];
      } else {
        brailleText += textToBraille[text[i]];
      }
    }
  }

  return brailleText;
}

function convertToText(braille) {
  let text = "";
  isNum = false;
  isCap = false;

  for (let i = 0; i < braille.length; i += 6) {
    let brailleChar = braille.slice(i, i + 6);

    if (!isNum) {
      //if isNum is false
      if (brailleToText[brailleChar] == "isNumb") {
        isNum = true;
      } else {
        if (!isCap) {
          if (brailleToText[brailleChar] == "isCapt") {
            isCap = true;
          } else {
            text += brailleToText[brailleChar];
          }
        } else {
          text += brailleToText[brailleChar].toUpperCase();
          isCap = false;
        }
      }
    } else {
      //if isNum is true
      if (brailleToText[brailleChar] == " ") {
        text += brailleToText[brailleChar];
        isNum = false;
      } else {
        text += brailleToNum[brailleChar];
      }
    }
  }

  return text;
}

if (isBraille(args)) {
  const result = convertToText(args);
  console.log(result);
} else {
  const result = convertToBraille(args);
  console.log(result);
}
