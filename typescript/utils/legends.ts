export const BRAILLE_TO_ENGLISH: { [brailleCharacter: string]: string } = {
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
  "OO.O.O": "n",
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
  "......": " ",
  ".....O": "capitalPrefix",
  ".O.OOO": "numberPrefix",
};

export const ENGLISH_TO_BRAILLE = generateEnglishToBrailleLegend();
export const NUMBER_TO_BRAILLE = generateNumberToBrailleLegend();
export const BRAILLE_TO_NUMBER = generateBrailleToNumberLegend();

function generateEnglishToBrailleLegend() {
  const brailleToEnglish: { [englishCharacter: string]: string } = {};

  for (const key in BRAILLE_TO_ENGLISH) {
    const value = BRAILLE_TO_ENGLISH[key];
    brailleToEnglish[value] = key;
  }

  return brailleToEnglish;
}

function generateNumberToBrailleLegend() {
  const brailleNumberChars = "jabcdefghi";
  const numberToBraille = [];

  for (let idx = 0; idx < brailleNumberChars.length; idx += 1) {
    const currentChar = brailleNumberChars[idx];
    numberToBraille.push(ENGLISH_TO_BRAILLE[currentChar]);
  }

  return numberToBraille;
}

function generateBrailleToNumberLegend() {
  const brailleToNumber: { [number: string]: string } = {};

  NUMBER_TO_BRAILLE.forEach((letter, index) => {
    brailleToNumber[letter] = String(index);
  });

  return brailleToNumber;
}
