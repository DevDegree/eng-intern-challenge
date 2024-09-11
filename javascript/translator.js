// create libraries
const english = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "0",
  "capitalFollows",
  "numberFollows",
  ".",
  ",",
  "?",
  "!",
  ":",
  ";",
  "-",
  "/",
  "<",
  ">",
  "(",
  ")",
  " ",
];

const braille = [
  "O.....",
  "O.O...",
  "OO....",
  "OO.O..",
  "O..O..",
  "OOO...",
  "OOOO..",
  "O.OO..",
  ".OO...",
  ".OOO..",
  "O...O.",
  "O.O.O.",
  "OO..O.",
  "OO.OO.",
  "O..OO.",
  "OOO.O.",
  "OOOOO.",
  "O.OOO.",
  ".OO.O.",
  ".OOOO.",
  "O...OO",
  "O.O.OO",
  ".OOO.O",
  "OO..OO",
  "OO.OOO",
  "O..OOO",
  "O.....",
  "O.O...",
  "OO....",
  "OO.O..",
  "O..O..",
  "OOO...",
  "OOOO..",
  "O.OO..",
  ".OO...",
  ".OOO..",
  ".....O",
  ".O.OOO",
  "..OO.O",
  "..O...",
  "..O.OO",
  "..OOO.",
  "..OO..",
  "..O.O.",
  "....OO",
  ".O..O.",
  ".O.O.O",
  ".O.O.O.",
  "O.O..O",
  ".O.OO.",
  "......",
];

const languageMap = new Map();

const checkIfIsBraille = (arr) => {
  // Check specifically for inputs that only have O and .
  // Based on test cases, process.arg will come in as a single item array if it is braille, but check with .every either way
  let brailleCheck = /^[O.]*$/;
  return arr.every((str) => brailleCheck.test(str));
};

function translateToBraille(input) {
  let number = false;
  let firstNumber = true;
  let capital = false;
  let wordArr = [];

  let str = input.join(" ");

  for (let i = 0; i < english.length; i++) {
    languageMap.set(english[i], braille[i]);
  }

  for (let i = 0; i < str.length; i++) {
    wordArr.push(str[i]);
  }

  let result = wordArr.map((letter) => {
    // capital if it's the same value uppercase, isn't a space and isn't a number
    if (letter === letter.toUpperCase() && letter !== " " && isNaN(letter)) {
      capital = true;
    }

    // if not a number and firstNumber is false
    if (!isNaN(letter) && firstNumber) {
      number = true;
    }

    // reset firstNumber after a space
    if (letter === " ") {
      firstNumber = true;
      number = false;
    }

    // trigger firstNumber so that the following numbers don't add the numberFollows braille
    if (number && firstNumber) {
      let preNumber =
        languageMap.get("numberFollows") + languageMap.get(letter);
      firstNumber = false;
      return preNumber;
    }

    if (capital) {
      let preCapital =
        languageMap.get("capitalFollows") +
        languageMap.get(letter.toLowerCase());
      capital = false;
      return preCapital;
    }

    return languageMap.get(letter);
  });

  return result.join("");
}

function translateToEnglish(input) {
  let number = false;
  let capital = false;
  let wordArr = [];

  // need to retrieve chunks of 6 for the braille translation
  for (let i = 0; i < input[0].length; i += 6) {
    wordArr.push(input[0].slice(i, i + 6));
  }

  for (let i = 0; i < braille.length; i++) {
    const currentValue = languageMap.get(braille[i]);

    if (currentValue) {
      languageMap.set(braille[i], [currentValue, english[i]]);
    } else {
      languageMap.set(braille[i], english[i]);
    }
  }

  let result = wordArr.map((letter) => {
    // capital check
    if (letter == ".....O") {
      capital = true;
      return;
    }

    // number check
    if (letter == ".O.OOO") {
      number = true;
      return;
    }

    // space check
    if (letter == "......") {
      number = false;
    }

    // a-j and 0-9 come in the form of array, check to select 0th or 1st index
    let val = languageMap.get(letter);

    if (Array.isArray(val)) {
      if (capital) {
        capital = false;
        return languageMap.get(letter)[0].toUpperCase();
      }
      if (number) {
        return languageMap.get(letter)[1];
      }
      return val[0];
    } else if (capital) {
      capital = false;
      return languageMap.get(letter)[0].toUpperCase();
    }
    return val;
  });
  return result.join("");
}

function translate() {
  const input = process.argv.slice(2); // array of what has been inputted
  const isBraille = checkIfIsBraille(input);

  if (input.length === 0) return;

  if (isBraille) {
    return translateToEnglish(input);
  } else {
    return translateToBraille(input);
  }
}

console.log(translate());
