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
    br: "......",
    en: " ",
  },
  //   {
  //     br: "..OO.O",
  //     en: ".",
  //   },
  //   {
  //     br: "..O...",
  //     en: ",",
  //   },
  //   {
  //     br: "..O.OO",
  //     en: "?",
  //   },
  //   {
  //     br: "..OOO.",
  //     en: "!",
  //   },
  //   {
  //     br: "..OO..",
  //     en: ":",
  //   },
  //   {
  //     br: "..O.O.",
  //     en: ";",
  //   },
  //   {
  //     br: "....OO",
  //     en: "-",
  //   },
  //   {
  //     br: ".O..O.",
  //     en: "/",
  //   },
  //   {
  //     br: ".OO..O",
  //     en: "<",
  //   },
  //   {
  //     br: "O..OO.",
  //     en: ">",
  //   },
  //   {
  //     br: "O.O..O",
  //     en: "(",
  //   },
  //   {
  //     br: ".O.OO.",
  //     en: ")",
  //   },
];

//Helper functions for checking language, character type
function isBraille(string) {
  for (const char of string) if (!(char === "O" || char === ".")) return false;

  if (string.length % 6 !== 0) {
    console.error("Unable to translate to English.");
    return false;
  } else return true;
}
function isEnglish(string) {
  for (const char of string)
    if (!(isLetter(char) || isNumeric(char)) && char !== (" " || ".")) {
      console.error("Unable to translate to Braille.");
      return false;
    } else return true;
}
const isNumeric = (char) => /\d/.test(char);
const isLetter = (char) => /[a-zA-Z]/.test(char);
const isUppercase = (char) => /[A-Z]/.test(char);

//Translate English <---> Braille
function translate(string) {
  if (isBraille(string)) {
    const brChars = [];
    let brString = string;
    let enString = "";

    while (brString.length > 0) {
      brChars.push(brString.slice(0, 6));
      brString = brString.slice(6);
    }

    brChars.forEach((brChar, i) => {
      if (brChar === ".....O") {
        enString += "";
      } else if (brChars[i - 1] === ".....O") {
        const charObj = alphabet.find((char) => char.br === brChar);
        enString += charObj.en.toUpperCase();
        console.log(enString);
      }
    });
  } else if (isEnglish(string)) {
    let enStr = string;
    const engChars = enStr.split("");
    let brStr = "";

    engChars.forEach((engChar, i) => {
      if (isEnglish()) {
      } else if (isNumeric(engChar)) {
        if (isLetter(engChars[i - 1]) || engChars[i - 1] === " ")
          brStr += ".O.OOO";
        const numObj = alphabet.find((char) => char.num == engChar);
        brStr += numObj.br;
      } else {
        if (isUppercase(engChar)) brStr += ".....O";
        const charObj = alphabet.find(
          (char) => char.en === engChar.toLowerCase()
        );
        brStr += charObj.br;
      }
    });

    console.log(enStr, enStr.length, brStr, brStr.length);
  } else {
    console.error("Unknown language.", error);
  }
}

// translate("Hello World");
// translate("1234 abc");
// translate("Giv3 it a try");
// translate("Zebra123");
// translate("TEST case");
// translate("code 2024");
// translate("No Braille Here");
// translate("A1B2C3D4");
// translate("A1b2c3D4");
// translate("thisIsALongString");
// translate("JavaScript42");

//
translate(
  ".....OO......O.OOOO..........OO.O....O.OOOO.O........OOO.....O.OOOOO.........OOO.O...O.OOOOO.O.."
);
// translate(
//   ".....OO......O.OOOO..........OO.O....O.OOOO.O........OOO.....O.OOOOO.........OOO.O...O.OOOOO.O..O"
// );
// translate(
//   ".....OO......O.OOOO..........OO.O....O.OOOO.O........OOO.....0.OOOOO.........OOO.O...O.OOOOO.O.."
// );
// translate(
//   ".....OOO.OO.O..OO............OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.............OO.OO..O..O..O.OOO.O..O.."
// );
// translate(
//   ".....OO.OO.O..OO............OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.............OO.OO..O..O..O.OOO.O..O.."
// );
