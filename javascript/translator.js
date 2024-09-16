// Shopify Translation App (Intern Challenge)
// Author: Jolson Eric Cruz

const brailleToLetters = new Map(); // Create a new Map object to store braille-letters key-value pairs.
brailleToLetters.set("O.....", "A");
brailleToLetters.set("O.O...", "B");
brailleToLetters.set("OO....", "C");
brailleToLetters.set("OO.O..", "D");
brailleToLetters.set("O..O..", "E");
brailleToLetters.set("OOO...", "F");
brailleToLetters.set("OOOO..", "G");
brailleToLetters.set("O.OO..", "H");
brailleToLetters.set(".OO...", "I");
brailleToLetters.set(".OOO..", "J");
brailleToLetters.set("O...O.", "K");
brailleToLetters.set("O.O.O.", "L");
brailleToLetters.set("OO..O.", "M");
brailleToLetters.set("OO.OO.", "N");
brailleToLetters.set("O..OO.", "O");
brailleToLetters.set("OOO.O.", "P");
brailleToLetters.set("OOOOO.", "Q");
brailleToLetters.set("O.OOO.", "R");
brailleToLetters.set(".OO.O.", "S");
brailleToLetters.set(".OOOO.", "T");
brailleToLetters.set("O...OO", "U");
brailleToLetters.set("O.O.OO", "V");
brailleToLetters.set(".OOO.O", "W");
brailleToLetters.set("OO..OO", "X");
brailleToLetters.set("OO.OOO", "Y");
brailleToLetters.set("O..OOO", "Z");

const brailleToNumbers = new Map(); // Create a new Map object to store braille-numbers key-value pairs.
brailleToNumbers.set("O.....", "1");
brailleToNumbers.set("O.O...", "2");
brailleToNumbers.set("OO....", "3");
brailleToNumbers.set("OO.O..", "4");
brailleToNumbers.set("O..O..", "5");
brailleToNumbers.set("OOO...", "6");
brailleToNumbers.set("OOOO..", "7");
brailleToNumbers.set("O.OO..", "8");
brailleToNumbers.set(".OO...", "9");
brailleToNumbers.set(".OOO..", "0");

const brailleToDecimal = new Map(); // Create a new Map object to store braille-decimal key-value pairs.
brailleToDecimal.set("..OO.O", ".");
brailleToDecimal.set("..O...", ",");
brailleToDecimal.set("..O.OO", "?");
brailleToDecimal.set("..OOO.", "!");
brailleToDecimal.set("..OO..", ":");
brailleToDecimal.set("..O.O.", ";");
brailleToDecimal.set("....OO", "-");
brailleToDecimal.set(".O..O.", "/");
brailleToDecimal.set(".OO..O", "<");
brailleToDecimal.set("O..OO.", ">");
brailleToDecimal.set("O.O..O", "(");
brailleToDecimal.set(".O.OO.", ")");

const lettersToBraille = new Map(); // Create a new Map object to store letters-braille key-value pairs.
const numbersToBraille = new Map(); // Create a new Map object to store numbers-braille key-value pairs.
const decimalToBraille = new Map(); // Create a new Map object to store decimal-braille key-value pairs.

// Iterate and populate each Map object with the corresponding key-value pairs.
for (let [braille, letter] of brailleToLetters) {
  lettersToBraille.set(letter, braille);
}
for (let [braille, number] of brailleToNumbers) {
  numbersToBraille.set(number, braille);
}
for (let [braille, decimal] of brailleToDecimal) {
  decimalToBraille.set(decimal, braille);
}

const args = process.argv.slice(2).join(" "); // Get runtime arguments and discard the first two elements ('node' and 'translator.js').

function translate(args) {
  const regex = /^[.O]+$/;
  let returnString = "";
  let numberFlag = false;
  let capitalFlag = false;
  let decimalFlag = false;

  if (regex.test(args)) {
    // Braille detected
    for (let i = 0; i < args.length; i += 6) {
      const braille = args.slice(i, i + 6);
      if (braille === "......") {
        numberFlag = false;
        returnString += " ";
      } else if (braille === ".O.OOO") numberFlag = true;
      else if (braille === ".....O") capitalFlag = true;
      else if (braille === ".O...O") decimalFlag = true;
      else if (numberFlag) returnString += brailleToNumbers.get(braille);
      else if (decimalFlag) {
        decimalFlag = false;
        returnString += brailleToDecimal.get(braille);
      } else if (capitalFlag) {
        capitalFlag = false;
        returnString += brailleToLetters.get(braille);
      } else returnString += brailleToLetters.get(braille).toLowerCase();
    }
  } else {
    // English detected
    for (let i = 0; i < args.length; i++) {
      if (args[i] === " ") {
        numberFlag = false;
        returnString += "......";
      } else if (args[i].match(/[0-9]/)) {
        if (!numberFlag) {
          numberFlag = true;
          returnString += ".O.OOO";
        }
        returnString += numbersToBraille.get(args[i]);
      } else if (args[i].match(/[a-z]/i)) {
        if (args[i] === args[i].toUpperCase()) returnString += ".....O";
        returnString += lettersToBraille.get(args[i].toUpperCase());
      } else if (args[i].match(/[.,?!:;\/<>()]/)) {
        returnString += ".O...O" + decimalToBraille.get(args[i]);
      }
    }
  }

  console.log(returnString);
}

translate(args);
