var letterToBraille = new Map();
letterToBraille.set("a", "O.....");
letterToBraille.set("b", "O.O...");
letterToBraille.set("c", "OO....");
letterToBraille.set("d", "OO.O..");
letterToBraille.set("e", "O..O..");
letterToBraille.set("f", "OOO...");
letterToBraille.set("g", "OOOO..");
letterToBraille.set("h", "O.OO..");
letterToBraille.set("i", ".OO...");
letterToBraille.set("j", ".OOO..");
letterToBraille.set("k", "O...O.");
letterToBraille.set("l", "O.O.O.");
letterToBraille.set("m", "OO..O.");
letterToBraille.set("n", "OO.OO.");
letterToBraille.set("o", "O..OO.");
letterToBraille.set("p", "OOO.O.");
letterToBraille.set("q", "OOOOO.");
letterToBraille.set("r", "O.OOO.");
letterToBraille.set("s", ".OO.O.");
letterToBraille.set("t", ".OOOO.");
letterToBraille.set("u", "O...OO");
letterToBraille.set("v", "O.O.OO");
letterToBraille.set("w", ".OOO.O");
letterToBraille.set("x", "OO..OO");
letterToBraille.set("y", "OO.OOO");
letterToBraille.set("z", "O..OOO");
var numberToBraille = new Map();
numberToBraille.set("1", "O.....");
numberToBraille.set("2", "O.O...");
numberToBraille.set("3", "OO....");
numberToBraille.set("4", "OO.O..");
numberToBraille.set("5", "O..O..");
numberToBraille.set("6", "OOO...");
numberToBraille.set("7", "OOOO..");
numberToBraille.set("8", "O.OO..");
numberToBraille.set("9", ".OO...");
numberToBraille.set("0", ".OOO..");
var specialCharToBraille = new Map();
specialCharToBraille.set(" ", "......");
specialCharToBraille.set("!", "..OOO.");
specialCharToBraille.set("?", "..O.OO");
specialCharToBraille.set(".", "..OO.O");
specialCharToBraille.set(",", "..O...");
specialCharToBraille.set(";", "..O.O.");
specialCharToBraille.set(":", "..OO..");
specialCharToBraille.set("-", "....OO");
specialCharToBraille.set("(", "O.O..O");
specialCharToBraille.set(")", ".O.OO.");
specialCharToBraille.set("/", ".O..O.");
specialCharToBraille.set("<", ".OO..O");
specialCharToBraille.set(">", "O..OO.");
var brailleToLetter = new Map();
brailleToLetter.set("O.....", "a");
brailleToLetter.set("O.O...", "b");
brailleToLetter.set("OO....", "c");
brailleToLetter.set("OO.O..", "d");
brailleToLetter.set("O..O..", "e");
brailleToLetter.set("OOO...", "f");
brailleToLetter.set("OOOO..", "g");
brailleToLetter.set("O.OO..", "h");
brailleToLetter.set(".OO...", "i");
brailleToLetter.set(".OOO..", "j");
brailleToLetter.set("O...O.", "k");
brailleToLetter.set("O.O.O.", "l");
brailleToLetter.set("OO..O.", "m");
brailleToLetter.set("OO.OO.", "n");
brailleToLetter.set("O..OO.", "o");
brailleToLetter.set("OOO.O.", "p");
brailleToLetter.set("OOOOO.", "q");
brailleToLetter.set("O.OOO.", "r");
brailleToLetter.set(".OO.O.", "s");
brailleToLetter.set(".OOOO.", "t");
brailleToLetter.set("O...OO", "u");
brailleToLetter.set("O.O.OO", "v");
brailleToLetter.set(".OOO.O", "w");
brailleToLetter.set("OO..OO", "x");
brailleToLetter.set("OO.OOO", "y");
brailleToLetter.set("O..OOO", "z");
var brailleToNumber = new Map();
brailleToNumber.set("O.....", "1");
brailleToNumber.set("O.O...", "2");
brailleToNumber.set("OO....", "3");
brailleToNumber.set("OO.O..", "4");
brailleToNumber.set("O..O..", "5");
brailleToNumber.set("OOO...", "6");
brailleToNumber.set("OOOO..", "7");
brailleToNumber.set("O.OO..", "8");
brailleToNumber.set(".OO...", "9");
brailleToNumber.set(".OOO..", "0");
var brailleToSpecialChar = new Map();
brailleToSpecialChar.set("......", " ");
brailleToSpecialChar.set("..OOO.", "!");
brailleToSpecialChar.set("..O.OO", "?");
brailleToSpecialChar.set("..OO.O", ".");
brailleToSpecialChar.set("..O...", ",");
brailleToSpecialChar.set("..O.O.", ";");
brailleToSpecialChar.set("..OO..", ":");
brailleToSpecialChar.set("....OO", "-");
brailleToSpecialChar.set("O.O..O", "(");
brailleToSpecialChar.set(".O.OO.", ")");
brailleToSpecialChar.set(".O..O.", "/");
brailleToSpecialChar.set(".OO..O", "<");
brailleToSpecialChar.set("O..OO.", ">");

const CAPITAL_LETTER_PREFIX = ".....O";
const NUMBER_PREFIX = ".O.OOO";
const DECIMAL_PREFIX = ".O...0";
const FULL_STOP_BRAILLE = "..OO.O";
const SPACE_BRAILLE = "......";
const MATRIX_CHAR_SIZE = 6;

interface Translation{
  translation: string,
  endIndex: number
}

function getEnglishCapChar(
  text: string, currentIndex: number
): Translation {
  let translation = "";
  let capChar = ""
  let braille = ""
  currentIndex += MATRIX_CHAR_SIZE;

  braille += text.substring(currentIndex, currentIndex + MATRIX_CHAR_SIZE);
  const value = brailleToLetter.get(braille);
  if (value === undefined) {
    throw new Error("An error occurred:" + braille + " Not found");
  }
  capChar += value.toUpperCase();

  let endIndex = currentIndex
  translation += capChar;
  return {
    translation,
    endIndex
  }
}


function getBrailleFromCapChar(
    text: string, currentIndex: number
  ): Translation {
    let translation = "";
    let braille = "" 

    braille += CAPITAL_LETTER_PREFIX;
    const brailleChar = letterToBraille.get(text.charAt(currentIndex).toLowerCase());
    if (brailleChar === undefined) {
      throw new Error("An error occurred: " + text.charAt(currentIndex).toLowerCase() + " Not found");
    }
    braille += brailleChar;

    translation += braille;
    let endIndex = currentIndex
    return {
      translation,
      endIndex
    }
}

function getNumberSequenceFromBraille(
    text: string, currentIndex: number
): Translation {

    let translation = "";
    let num = "";

    currentIndex += MATRIX_CHAR_SIZE;
  while (
   currentIndex < text.length &&
    text.substring(
      currentIndex,
      currentIndex + MATRIX_CHAR_SIZE,
    ) !== SPACE_BRAILLE
  ) {
    const brailleNumber = text.substring(
      currentIndex,
      currentIndex + MATRIX_CHAR_SIZE,
    );
    if (/\d/.test(brailleToNumber.get(brailleNumber))) {
      const value = brailleToNumber.get(brailleNumber);
      if (value === undefined) {
        throw new Error("An error occurred: " + brailleNumber + " Not found");
      }
      num += value;
    } else if (brailleNumber === DECIMAL_PREFIX) {
        const result = getDecimalFromBraille(text, currentIndex);
        num += result.translation;
        currentIndex = result.endIndex;
    } else {
        const result = getSpecialCharFromBraille(text, currentIndex);
        num += result.translation;
        currentIndex = result.endIndex;
    }
    currentIndex += MATRIX_CHAR_SIZE;
  }


  translation += num;
  let endIndex = currentIndex;
  if (endIndex < text.length) {
    const value = brailleToSpecialChar.get(SPACE_BRAILLE);
    if (value === undefined) {
      throw new Error("An error occurred: " + SPACE_BRAILLE + " Not found");
    }
    translation += value;
  }
  return {
    translation,
    endIndex
  }
}

function getBrailleFromNumberSequence(
    text: string, currentIndex: number
): Translation {
    let translation = "";
    let braille = "";

    braille += NUMBER_PREFIX;
  while (currentIndex < text.length && text.charAt(currentIndex) !== brailleToSpecialChar.get(SPACE_BRAILLE)) {
    if (/\d/.test(text.charAt( currentIndex))) {
      let char = text.charAt(currentIndex);
      const value = numberToBraille.get(char);
      if (value === undefined) {
        throw new Error("An error occurred: " + char + " Not found");
      }
      braille += value;
    } else if (text.charAt(currentIndex) === FULL_STOP_BRAILLE) {
        const result = getBrailleFromDecimal(text, currentIndex);
        braille += result.translation;
        currentIndex = result.endIndex;
    } else {
        const result = getBrailleFromSpecialChar(text, currentIndex);
        braille += result.translation;
        currentIndex = result.endIndex;
    }
    currentIndex++;
  }

    translation += braille;
    let endIndex = currentIndex;
  if (currentIndex < text.length) {
    translation += SPACE_BRAILLE;
  }
  return {
    translation,
    endIndex
  }
}

function getSpecialCharFromBraille(
    text: string, currentIndex: number
): Translation {
    let translation = "";
    let braille = "";
    let specialChar = "";

    braille += text.substring(currentIndex, currentIndex + MATRIX_CHAR_SIZE);
    const value = brailleToSpecialChar.get(braille);
    if (value === undefined) {
      throw new Error("An error occurred: " + braille + " Not found");
    }
    specialChar += value;
    

    translation += specialChar;
    let endIndex = currentIndex;
  return {
    translation,
    endIndex
  }
}

function getBrailleFromSpecialChar(
    text: string, currentIndex: number
): Translation {
    let translation = "";
    let braille = "";
    let specialChar = "";

    specialChar += text.charAt(currentIndex);
    const value = specialCharToBraille.get(specialChar);
    if (value === undefined) {
      throw new Error("An error occurred: " + specialChar + " Not found");
    }
    braille += value;

    translation += braille;
    let endIndex = currentIndex;
  return {
    translation,
    endIndex
  }
}

function getDecimalFromBraille(
    text: string, currentIndex: number
): Translation {
    let translation = "";
    let specialChar = "";

    currentIndex += MATRIX_CHAR_SIZE;
    const result = getSpecialCharFromBraille(text, currentIndex);
    specialChar += result.translation;
    currentIndex = result.endIndex;

    translation += result.translation;
    let endIndex = result.endIndex;
  return {
    translation,
    endIndex
  }
}

function getBrailleFromDecimal(
    text: string, currentIndex: number
): Translation {
    let translation = "";
    let braille = "";

    braille += DECIMAL_PREFIX;
    braille += getBrailleFromSpecialChar(text, currentIndex);

    translation += braille;
    let endIndex = currentIndex;
  return {
    translation,
    endIndex
  }
}

function brailleToEnglishFunction(text: string): string {
  var english = "";

  for (let i = 0; i < text.length; i += MATRIX_CHAR_SIZE) {
    const brailleCharater = text.substring(i, i + MATRIX_CHAR_SIZE);
    if (brailleCharater === CAPITAL_LETTER_PREFIX) {
      const result = getEnglishCapChar(text, i);  
      english += result.translation;
      i = result.endIndex;
    } else if (brailleCharater === NUMBER_PREFIX) {
      const result = getNumberSequenceFromBraille(text, i);
      english += result.translation;
      i = result.endIndex;
    } else if (brailleToLetter.has(brailleCharater)) {
      const value = brailleToLetter.get(brailleCharater);
      if (value === undefined) {
        throw new Error("An error occurred: " + brailleCharater + " Not found");
      }
      english += value;
    } else {
      const result = getSpecialCharFromBraille(text, i);
      english += result.translation;
      i = result.endIndex;
    }
  }

  return english;
}

function englishToBrailleFunction(text: string): string {
  if (/^[O.]+$/.test(text)) {
    throw new Error("Text could not be classified as English");
  }
  let braille = "";
  for (let i = 0; i < text.length; i++) {
    const char = text.charAt(i);
    if (/[A-Z]/.test(char)) {
      const result = getBrailleFromCapChar(text, i);
      braille += result.translation;
      i = result.endIndex;
    } else if (/\d/.test(char)) {
      const result = getBrailleFromNumberSequence(text, i);
      braille += result.translation;
      i = result.endIndex;
    } else if (/[^a-zA-Z0-9]/.test(char)) {
      const result = getBrailleFromSpecialChar(text, i);
      braille += result.translation;
      i = result.endIndex;
    } else {
      const value = letterToBraille.get(char);
      if (value === undefined) {
        throw new Error("An error occurred: " + char + " Not found");
      }
      braille += value;
    }
  }
  return braille;
}

function isBraille(text: string): boolean {
  return /^[O.]+$/.test(text) && text.length % 6 === 0;
}

function translator(text: string): string {
  if (text.length === 0) {
    return "";
  }
  return isBraille(text)
    ? brailleToEnglishFunction(text)
    : englishToBrailleFunction(text);
}

const args = process.argv.slice(2); 
const input = args.join(' ');
const tranlatedSting = translator(input);
console.log(tranlatedSting);

export { brailleToEnglishFunction, englishToBrailleFunction, translator };