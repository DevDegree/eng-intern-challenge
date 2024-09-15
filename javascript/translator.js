import {
  BRAILLE_SIGNS,
  BRAILLE_NUMBERS,
  BRAILLE_REFERENCE,
  BRAILLE_REGEX,
} from "./constants.js";

const isValidBraille = (input) =>
  input.length % 6 === 0 && BRAILLE_REGEX.test(input);

const isCapitalLetter = (input) => input >= "A" && input <= "Z";
const isNumericCharacter = (input) => input >= "0" && input <= "9";

const isCapitalBrailleModifier = (input) => input === BRAILLE_SIGNS[0].braille;
const isNumberBrailleModifier = (input) => input === BRAILLE_SIGNS[1].braille;

const convertToBraille = (alphanumeric) => {
  let result = "";
  let isNumberInputMode = false;

  for (const char of alphanumeric) {
    if (isCapitalLetter(char)) {
      result += BRAILLE_SIGNS[0].braille;
    } else if (isNumericCharacter(char)) {
      if (!isNumberInputMode) {
        isNumberInputMode = true;
        result += BRAILLE_SIGNS[1].braille;
      }

      const brailleNumber = BRAILLE_NUMBERS.find(
        (braille) => braille.value === char
      );

      if (brailleNumber) {
        result += brailleNumber.braille;
      }
      continue;
    }

    isNumberInputMode = false;

    const brailleCharacter = BRAILLE_REFERENCE.find(
      (reference) => reference.value === char.toLowerCase()
    );

    if (brailleCharacter) result += brailleCharacter.braille;
  }
  return result;
};

const convertToAlphanumeric = (braille) => {
  let result = "";
  let isNumberInputMode = false;
  let isCapitalInputMode = false;

  for (let i = 0; i < braille.length; i += 6) {
    const currentBrailleChar = braille.slice(i, i + 6);

    if (isCapitalBrailleModifier(currentBrailleChar)) {
      isCapitalInputMode = true;
      continue;
    }
    if (isNumberBrailleModifier(currentBrailleChar)) {
      isNumberInputMode = true;
      continue;
    }

    let index = BRAILLE_REFERENCE.findIndex((ref) => {
      return ref.braille === currentBrailleChar;
    });
    const currentValue = index !== -1 ? BRAILLE_REFERENCE[index].value : ""; // graceful error handling

    if (isNumberInputMode) {
      index = BRAILLE_NUMBERS.findIndex(
        (ref) => ref.braille === currentBrailleChar
      );

      if (index === -1) {
        isNumberInputMode = false;
        result += currentValue;
        continue;
      }
      result += BRAILLE_NUMBERS[index].value;
      continue;
    }

    result += isCapitalInputMode ? currentValue.toUpperCase() : currentValue;
    isCapitalInputMode = false;
  }

  return result;
};

const translator = (consoleInput) => {
  const isBrailleInput = isValidBraille(consoleInput);
  console.log(
    isBrailleInput
      ? convertToAlphanumeric(consoleInput)
      : convertToBraille(consoleInput)
  );
};

// Combine the command-line arguments
const inputArgs = process.argv.slice(2).join(" ");

// Run the command
translator(inputArgs);
