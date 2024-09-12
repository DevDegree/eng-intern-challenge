const ENGLISH_TO_BRAILLE = "ENGLISH TO BRAILLE";
const BRAILLE_TO_ENGLISH = "BRAILLE TO ENGLISH";

const UPPER_CASE_TYPE = "UPPER CASE";
const LOWER_CASE_TYPE = "LOWER CASE";
const NUMBER_TYPE = "NUMBER";
const SPECIAL_CHARACTER_TYPE = "SPECIAL CHARACTER";
const WHITESPACE_TYPE = "WHITESPACE";

const INVALID_BRAILLE_MESSAGE = "Invalid Braille String!";
const INVALID_ENGLISH_MESSAGE = "Invalid English String!";

const COMMA = ",";
const WHITESPACE = " ";

const DECISION_REGEX = new RegExp(/^[O.]*$/);

const MAP_BRAILLE_TO_ENGLISH_LETTER = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".OO.O.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
};

const MAP_BRAILLE_TO_ENGLISH_NUMBER = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const MAP_BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS = {
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

const MAP_ENGLISH_TO_BRAILLE_LETTER = {
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
};

const MAP_ENGLISH_TO_BRAILLE_NUMBER = {
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

const MAP_ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS = {
  ".": "..OO.O",
  ",": "..O...",
  "?": "..O.OO",
  "!": "..OOO.",
  ":": "..OO..",
  "-": "....OO",
  "/": ".O..O.",
  "<": ".OO..O",
  ">": "O..OO.",
  "(": "O.O..O",
  ")": ".O.OO.",
  " ": "......",
};

const CAPITAL_FOLLOWS = ".....O";
const DECIMAL_FOLLOWS = ".O...O";
const NUMBER_FOLLOWS = ".O.OOO";

const convertToBrailleCharacters = (str, length) => {
  const regex = new RegExp(`.{1,${length}}`, "g");
  return str.match(regex) || [];
};

const CheckEnglishCharacter = (character) => {
  if (character === WHITESPACE) {
    return WHITESPACE_TYPE;
  } else if (character >= "A" && character <= "Z") {
    return UPPER_CASE_TYPE;
  } else if (character >= "a" && character <= "z") {
    return LOWER_CASE_TYPE;
  } else if (character >= 0 && character <= 9) {
    return NUMBER_TYPE;
  } else {
    return SPECIAL_CHARACTER_TYPE;
  }
};

const CheckBrailleCharacter = (character) => {
  if (character === MAP_ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[WHITESPACE]) {
    return WHITESPACE_TYPE;
  } else if (character === CAPITAL_FOLLOWS) {
    return UPPER_CASE_TYPE;
  } else if (MAP_BRAILLE_TO_ENGLISH_LETTER.hasOwnProperty(character)) {
    return LOWER_CASE_TYPE;
  } else if (
    character === NUMBER_FOLLOWS ||
    MAP_BRAILLE_TO_ENGLISH_NUMBER.hasOwnProperty(character)
  ) {
    return NUMBER_TYPE;
  } else if (
    MAP_BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS.hasOwnProperty(character)
  ) {
    return SPECIAL_CHARACTER_TYPE;
  }
};

const ConvertBrailleToEnglish = () => {
  try {
    const inputBrailleCharacters = convertToBrailleCharacters(inputString, 6);

    let isCapital = false;
    let isNumber = false;
    let EnglishString = "";

    inputBrailleCharacters.forEach((character) => {
      let inputBrailleCharacterType = null;
      if (!isCapital || !isNumber) {
        inputBrailleCharacterType = CheckBrailleCharacter(character);
      }

      if (inputBrailleCharacterType === UPPER_CASE_TYPE) {
        isCapital = true;
        return;
      }
      if (!isNumber && inputBrailleCharacterType === NUMBER_TYPE) {
        isNumber = true;
        return;
      }
      if (isNumber && inputBrailleCharacterType === WHITESPACE_TYPE) {
        isNumber = false;
      }

      let EnglishCharacter = "";
      if (isCapital) {
        isCapital = false;
        EnglishCharacter =
          MAP_BRAILLE_TO_ENGLISH_LETTER[character].toUpperCase();
      } else if (isNumber) {
        EnglishCharacter = MAP_BRAILLE_TO_ENGLISH_NUMBER[character];
      } else if (inputBrailleCharacterType === LOWER_CASE_TYPE) {
        EnglishCharacter = MAP_BRAILLE_TO_ENGLISH_LETTER[character];
      } else if (inputBrailleCharacterType === NUMBER_TYPE) {
        EnglishCharacter = MAP_BRAILLE_TO_ENGLISH_NUMBER[character];
      } else {
        EnglishCharacter = MAP_BRAILLE_TO_ENGLISH_SPECIAL_CHARACTERS[character];
      }

      if (!EnglishCharacter) {
        throw new Error(INVALID_BRAILLE_MESSAGE);
      }

      EnglishString += EnglishCharacter;
    });

    console.log(EnglishString);
  } catch (error) {
    console.log(error.message);
  }
};

const ConvertEnglishToBraille = () => {
  try {
    const inputCharacters = inputString.split("");

    let isNumber = false;
    let BrailleString = "";
    inputCharacters.forEach((character) => {
      const characterType = CheckEnglishCharacter(character);

      let characterBraille = "";
      if (characterType === UPPER_CASE_TYPE) {
        characterBraille =
          CAPITAL_FOLLOWS +
          MAP_ENGLISH_TO_BRAILLE_LETTER[character.toLowerCase()];
      } else if (characterType === LOWER_CASE_TYPE) {
        characterBraille = MAP_ENGLISH_TO_BRAILLE_LETTER[character];
      } else if (characterType === NUMBER_TYPE) {
        if (!isNumber) {
          characterBraille =
            NUMBER_FOLLOWS + MAP_ENGLISH_TO_BRAILLE_NUMBER[character];
          isNumber = true;
        } else {
          characterBraille = MAP_ENGLISH_TO_BRAILLE_NUMBER[character];
        }
      } else if (characterType === WHITESPACE_TYPE) {
        characterBraille = MAP_ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[character];
        isNumber = isNumber === true;
      } else if (characterType === SPECIAL_CHARACTER_TYPE) {
        characterBraille = MAP_ENGLISH_TO_BRAILLE_SPECIAL_CHARACTERS[character];
      }

      if (!characterBraille) {
        throw new Error(INVALID_ENGLISH_MESSAGE);
      }

      BrailleString += characterBraille;
    });

    console.log(BrailleString);
  } catch (error) {
    console.log(error.message);
  }
};

const inputArray = process.argv.splice(2);

if (inputArray.length === 0) {
  return;
}

const inputString = inputArray.toString().replaceAll(COMMA, WHITESPACE);

if (DECISION_REGEX.test(inputString)) {
  ConvertBrailleToEnglish();
} else {
  ConvertEnglishToBraille();
}
