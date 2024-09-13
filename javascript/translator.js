#!/usr/bin/env node

//Arrays for character conversion & testing
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
const testStrings = [
  {
    en: "Hello World",
    br: ".....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..",
  },
  {
    en: "1234 abc",
    br: ".O.OOOO.....O.O...OO....OO.O........O.....O.O...OO....",
  },
  {
    en: "Giv3 it a try",
    br: ".....OOOOO...OO...O.O.OO.O.OOOOO...........OO....OOOO.......O............OOOO.O.OOO.OO.OOO",
  },
  {
    en: "Zebra123",
    br: ".....OO..OOOO..O..O.O...O.OOO.O......O.OOOO.....O.O...OO....",
  },
  {
    en: "TEST case",
    br: ".....O.OOOO......OO..O.......O.OO.O......O.OOOO.......OO....O......OO.O.O..O..",
  },
  {
    en: "code 2024",
    br: "OO....O..OO.OO.O..O..O.........O.OOOO.O....OOO..O.O...OO.O..",
  },
  {
    en: "No Braille Here",
    br: ".....OOO.OO.O..OO............OO.O...O.OOO.O......OO...O.O.O.O.O.O.O..O.............OO.OO..O..O..O.OOO.O..O..",
  },
  {
    en: "A1B2C3D4",
    br: ".....OO......O.OOOO..........OO.O....O.OOOO.O........OOO.....O.OOOOO.........OOO.O...O.OOOOO.O..",
  },
  {
    en: "A1b2c3D4",
    br: ".....OO......O.OOOO.....O.O....O.OOOO.O...OO.....O.OOOOO.........OOO.O...O.OOOOO.O..",
  },
  {
    en: "thisIsALongString",
    br: ".OOOO.O.OO...OO....OO.O......O.OO....OO.O......OO..........OO.O.O.O..OO.OO.OO.OOOO.......O.OO.O..OOOO.O.OOO..OO...OO.OO.OOOO..",
  },
  {
    en: "The time is 1234 PM",
    br: ".....O.OOOO.O.OO..O..O.........OOOO..OO...OO..O.O..O.........OO....OO.O........O.OOOO.....O.O...OO....OO.O.............OOOO.O......OOO..O.",
  },
  {
    en: "123 apples and 456 oranges",
    br: ".O.OOOO.....O.O...OO..........O.....OOO.O.OOO.O.O.O.O.O..O...OO.O.......O.....OO.OO.OO.O.........O.OOOOO.O..O..O..OOO.........O..OO.O.OOO.O.....OO.OO.OOOO..O..O...OO.O.",
  },
  {
    en: "A12B3 has 50 items in total",
    br: ".....OO......O.OOOO.....O.O........OO.O....O.OOOOO..........O.OO..O......OO.O........O.OOOO..O...OOO.........OO....OOOO.O..O..OO..O..OO.O........OO...OO.OO........OOOO.O..OO..OOOO.O.....O.O.O.",
  },
  {
    en: "I live at 1234 Elm St, Apt 5A",
    br: ".....O.OO.........O.O.O..OO...O.O.OOO..O........O......OOOO........O.OOOO.....O.O...OO....OO.O.............OO..O..O.O.O.OO..O............O.OO.O..OOOO...O..............OO.....OOO.O..OOOO........O.OOOO..O.......OO.....",
  },
  {
    en: "Numbers 10 20 30 appear here",
    br: ".....OOO.OO.O...OOOO..O.O.O...O..O..O.OOO..OO.O........O.OOOO......OOO.........O.OOOO.O....OOO.........O.OOOOO.....OOO........O.....OOO.O.OOO.O.O..O..O.....O.OOO.......O.OO..O..O..O.OOO.O..O..",
  },
];

//Helper functions & RegExps for checking language, character type
function isBraille(string) {
  for (const char of string) if (!(char === "O" || char === ".")) return false;

  if (string.length % 6 !== 0) {
    console.error("Corrupt input. Unable to translate to English.");
    return false;
  } else return true;
}
const isNumeric = (char) => /\d/.test(char);
const isLetter = (char) => /[a-zA-Z]/.test(char);
const isUppercase = (char) => /[A-Z]/.test(char);
const isEnglish = (char) => /\w|\s[[:punct:]]|/.test(char);

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
    console.log(brString, brString.length, enString, enString.length);
  } else {
    let enStr = string;
    let brStr = "";
    const engChars = enStr.split("");

    engChars.forEach((engChar, i) => {
      if (!isEnglish(engChar)) {
        console.error("Unknown language, unable to translate.", error);
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
    console.log(brStr);
  }
}

testStrings.forEach((testString) => {
  translate(testString.br);
});
