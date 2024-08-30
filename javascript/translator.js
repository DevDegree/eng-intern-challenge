import {
  brailleLetterMap,
  brailleNumberMap,
  brailleSpecialMap,
} from "./braille-dictionary.js";
import {
  isDigit,
  isUppercase,
  splitIntoBrailleCells,
  detectInputType,
  findCharacterInMap,
} from "./utils.js";
import { validateBrailleInput } from "./validation.js";

function translateToBraille(text) {
  let brailleTranslation = "";
  let isInNumberMode = false;

  for (let character of text) {
    if (isDigit(character)) {
      if (!isInNumberMode) {
        brailleTranslation += brailleSpecialMap["number"];
        isInNumberMode = true;
      }
      brailleTranslation += brailleNumberMap[character];
    } else {
      if (isInNumberMode) {
        isInNumberMode = false;
      }

      if (isUppercase(character)) {
        brailleTranslation += brailleSpecialMap["capital"];
        character = character.toLowerCase();
      }

      brailleTranslation += brailleLetterMap[character] || "";
    }
  }

  return brailleTranslation;
}

function translateToEnglish(braille) {
  validateBrailleInput(braille);

  let englishTranslation = "";
  let isInNumberMode = false;
  let shouldCapitalizeNext = false;

  const brailleCells = splitIntoBrailleCells(braille);

  for (let cell of brailleCells) {
    if (cell === brailleSpecialMap["number"]) {
      isInNumberMode = true;
      continue;
    }

    if (cell === brailleLetterMap[" "]) {
      isInNumberMode = false;
      englishTranslation += " ";
      continue;
    }

    if (cell === brailleSpecialMap["capital"]) {
      shouldCapitalizeNext = true;
      continue;
    }

    let translatedCharacter = isInNumberMode
      ? findCharacterInMap(brailleNumberMap, cell)
      : findCharacterInMap(brailleLetterMap, cell);

    if (shouldCapitalizeNext && translatedCharacter) {
      translatedCharacter = translatedCharacter.toUpperCase();
      shouldCapitalizeNext = false;
    }

    englishTranslation += translatedCharacter || "";
  }

  return englishTranslation.trim();
}


function translate(input) {
  const inputType = detectInputType(input);
  return inputType === "english"
    ? translateToBraille(input)
    : translateToEnglish(input);
}

const inputText = process.argv.slice(2).join(" ");
if (inputText) {
  try {
    console.log(translate(inputText));
  } catch (error) {
    console.error("Translation error:", error.message);
  }
} else {
  console.log("Please provide text to translate.");
}
