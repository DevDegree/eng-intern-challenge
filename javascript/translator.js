#!/usr/bin/env node
const input = process.argv.slice(2).join(" ");

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

//Helper functions to check language of string rec'd as input
function isBraille(string) {
  for (const char of string) if (!(char === "O" || char === ".")) return false;

  if (string.length % 6 !== 0) {
    return false;
  } else return true;
}
const isEnglish = (char) => /\w|\s[[:punct:]]|/.test(char);
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
      const brCharObj = alphabet.find((char) => char.br === brChar);

      if (brChar === "......") enString += brCharObj.en;
      else if (brChar === ".....O" || brChar === ".O.OOO") {
        enString += "";
      } else if (brChars[i - 1] === ".....O") {
        enString += brCharObj.en.toUpperCase();
      } else if (
        brChars[i - 1] === ".O.OOO" ||
        (isNumeric(enString.charAt(enString.length - 1)) &&
          brChars[i + 1] !== ".O.OOO")
      ) {
        enString += brCharObj.num;
      } else {
        enString += brCharObj.en;
      }
    });
    console.log(enString);
  } else {
    let enStr = string;
    let brStr = "";
    const engChars = enStr.split("");

    engChars.forEach((engChar, i) => {
      if (isNumeric(engChar)) {
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
    console.log(brStr);
  }
}
translate(input);
