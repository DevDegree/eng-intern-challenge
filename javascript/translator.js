#!/usr/bin/env node

const BRAILLE_TO_ENGLISH = {
  "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
  "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
  ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
  "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
  "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
  "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
  "OO.OOO": "y", "O..OOO": "z", 
  ".....O": "capital", ".O.OOO": "number", "......": " "
};

const ENGLISH_TO_BRAILLE = {
  "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
  "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
  "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
  "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
  "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
  "z": "O..OOO", "A": ".....O O.....", "B": ".....O O.O...", "C": ".....O OO....",
  "D": ".....O OO.O..", "E": ".....O O..O..", "F": ".....O OOO...", "G": ".....O OOOO..",
  "H": ".....O O.OO..", "I": ".....O .OO...", "J": ".....O .OOO..", "K": ".....O O...O.",
  "L": ".....O O.O.O.", "M": ".....O OO..O.", "N": ".....O OO.OO.", "O": ".....O O..OO.",
  "P": ".....O OOO.O.", "Q": ".....O OOOOO.", "R": ".....O O.OOO.", "S": ".....O .OO.O.",
  "T": ".....O .OOOO.", "U": ".....O O...OO", "V": ".....O O.O.OO", "W": ".....O .OOO.O",
  "X": ".....O OO..OO", "Y": ".....O OO.OOO", "Z": ".....O O..OOO", "1": ".O.OOO O.....",
  "2": ".O.OOO O.O...", "3": ".O.OOO OO....", "4": ".O.OOO OO.O..", "5": ".O.OOO O..O..",
  "6": ".O.OOO OOO...", "7": ".O.OOO OOOO..", "8": ".O.OOO O.OO..", "9": ".O.OOO .OO...",
  "0": ".O.OOO .OOO.."
};

function brailleToEnglish(input) {
  const words = input.split(' ');
  let result = [];
  let numberMode = false;
  let capitalMode = false;

  words.forEach(word => {
    const letters = word.match(/.{6}/g) || [];
    let translatedWord = [];

    letters.forEach(letter => {
      if (letter === ".....O") {
        capitalMode = true;
      } else if (letter === ".O.OOO") {
        numberMode = true;
      } else {
        let char = BRAILLE_TO_ENGLISH[letter];

        if (capitalMode) {
          char = char.toUpperCase();
          capitalMode = false;
        }

        if (numberMode && /[a-j]/.test(char)) {
          char = String.fromCharCode(char.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
          numberMode = false;
        } else if (char === " ") {
          numberMode = false;
        }

        translatedWord.push(char);
      }
    });

    result.push(translatedWord.join(''));
  });

  return result.join(' ');
}
function englishToBraille(input) {
  let result = [];
  let numberMode = false;

  for (let i = 0; i < input.length; i++) {
    let char = input[i];

    if (/[A-Z]/.test(char)) {
      result.push(".....O");
      char = char.toLowerCase();
    }

    if (/[0-9]/.test(char)) {
      if (!numberMode) {
        result.push(".O.OOO");
        numberMode = true;
      }
      char = String.fromCharCode(char.charCodeAt(0) + 'a'.charCodeAt(0) - '1'.charCodeAt(0));
    } else {
      numberMode = false; 
    }

    if (ENGLISH_TO_BRAILLE[char]) {
      result.push(ENGLISH_TO_BRAILLE[char]);
    } else {
      result.push("......");
    }
  }

  return result.join('');
}


function translate(input) {
  if (/^[O\.]+$/.test(input)) {
    console.log(brailleToEnglish(input));
  } else {
    console.log(englishToBraille(input));
  }
}

const input = process.argv.slice(2).join(' ');
if (input) {
  translate(input);
} else {
  console.log("Usage: node translator.js [text_to_translate]");
}
