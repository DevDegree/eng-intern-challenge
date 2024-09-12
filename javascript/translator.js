#!/usr/bin/env node

const alphabet = [
  {
    br: "O.....",
    en: "a",
    num: 1,
  },
  {
    br: "O.O...",
    en: "b",
    num: 2,
  },
  {
    br: "OO....",
    en: "c",
    num: 3,
  },
  {
    br: "OO.O..",
    en: "d",
    num: 4,
  },
  {
    br: "O..O..",
    en: "e",
    num: 5,
  },
  {
    br: "OOO...",
    en: "f",
    num: 6,
  },
  {
    br: "OOOO..",
    en: "g",
    num: 7,
  },
  {
    br: "O.OO..",
    en: "h",
    num: 8,
  },
  {
    br: ".OO...",
    en: "i",
    num: 9,
  },
  {
    br: ".OOO..",
    en: "j",
    num: 0,
  },
  {
    br: "O...O.",
    en: "k",
  },
  {
    br: "O.O.O.",
    en: "l",
  },
  {
    br: "OO..O.",
    en: "m",
  },
  {
    br: "OO.OO.",
    en: "n",
  },
  {
    br: "O..OO.",
    en: "o",
  },
  {
    br: "OOO.O.",
    en: "p",
  },
  {
    br: "OOOOO.",
    en: "q",
  },
  {
    br: "O.OOO.",
    en: "r",
  },
  {
    br: ".OO.O.",
    en: "s",
  },
  {
    br: ".OOOO.",
    en: "t",
  },
  {
    br: "O...OO",
    en: "u",
  },
  {
    br: "O.O.OO",
    en: "v",
  },
  {
    br: ".OOO.O",
    en: "w",
  },
  {
    br: "OO..OO",
    en: "x",
  },
  {
    br: "OO.OOO",
    en: "y",
  },
  {
    br: "O..OOO",
    en: "z",
  },
  {
    br: "..OO.O",
    en: ".",
  },
  {
    br: "..O...",
    en: ",",
  },
  {
    br: "..O.OO",
    en: "?",
  },
  {
    br: "..OOO.",
    en: "!",
  },
  {
    br: "..OO..",
    en: ":",
  },
  {
    br: "..O.O.",
    en: ";",
  },
  {
    br: "....OO",
    en: "-",
  },
  {
    br: ".O..O.",
    en: "/",
  },
  {
    br: ".OO..O",
    en: "<",
  },
  {
    br: "O..OO.",
    en: ">",
  },
  {
    br: "O.O..O",
    en: "(",
  },
  {
    br: ".O.OO.",
    en: ")",
  },
  {
    br: "......",
    en: " ",
  },
];

function isBraille(string) {
  if (string.length % 6 !== 0) {
    return false;
  } else {
    for (const char of string) {
      if (!(char === "O" || char === ".")) {
        return false;
      } else {
        return true;
      }
    }
  }
}

const isNumeric = (char) => /\d/.test(char);
const isUppercase = (char) => /[A-Z]/.test(char);
// function isUppercase(char) {
//   if (isAlpha(char) && char === char.toUpperCase()) {
//     return true;
//   } else {
//     return false;
//   }
// }

function translate(stringToTranslate) {
  if (isBraille(stringToTranslate)) {
    console.log(stringToTranslate);
  } else {
    const engChars = stringToTranslate.split("");
    let brailleStr = "";

    engChars.forEach((engChar, i) => {
      if (isNumeric(engChar)) {
        if (!isNumeric(engChars[i - 1])) {
          brailleStr += ".O.OOO";
        } else {
          brailleStr += "";
        }
        const numObj = alphabet.find((char) => char.num == engChar);
        brailleStr += numObj.br;
      } else {
        if (isUppercase(engChar)) {
          brailleStr += ".....O";
        } else {
          brailleStr += "";
        }
        const charObj = alphabet.find(
          (char) => char.en === engChar.toLowerCase()
        );
        brailleStr += charObj.br;
      }
    });

    console.log(brailleStr, brailleStr.length);
  }
}

// translate("Hello, (good) morning");
// translate("123");
// translate("12 ");
// translate("heLlO 2");
// translate("  2 fg4");
// translate("hello");
// translate("Hello");
// translate("HELLO");
