const brailleCharacters = {
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
  ".....O": "^", // Indicates that the following letter is capitalized
  ".O...O": ".", // Indicates that the point is for decimal numbers
  ".O.OOO": "#", // Indicates that the following characters are numbers
  "..OO.O": ".",
  "..O...": ",",
  "..O.OO": "?",
  "..OOO.": "!",
  "..OO..": ":",
  "..O.O.": ";",
  "....OO": "-",
  ".O..O.": "/",
  ".OO..O": "<",
  "O..OO.": ">",
  "O.O..O": "(",
  ".O.OO.": ")",
  "......": " ",
};

function brailleToEnglish(brailleTxt) {
  // Starting the variables
  let englishText = "";
  let numbersFollows = false; // is it numbers mode?
  let capitalFollows = false; // is it uppercase mode?

  // Split the Braille text into sequences of 6 characters
  const charactersBraille = brailleTxt.match(/.{1,6}/g);

  charactersBraille.forEach((char) => {
    if (char === ".....O") {
      capitalFollows = true; // Activate uppercase mode
    } else if (char === ".O.OOO") {
      numbersFollows = true; // Activate numebrs mode
    } else if (char === ".O...O" && numbersFollows) {
      englishText += "."; // Add a decimal point in numeric mode
    } else if (brailleCharacters[char]) {
      let letters = brailleCharacters[char];
      if (capitalFollows) {
        letters = letters.toUppercase(); // Convert the letters to uppercase
        capitalFollows = false; // Disable uppercase mode after a letter
      }
      englishText += letters;
      numbersFollows = false; // Disables number mode after added it
    }
  });
}
