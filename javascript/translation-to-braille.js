import {
  ENGLISH_TO_BRAILLE_MAPPINGS,
  NUMBERS_TO_BRAILLE_MAPPINGS,
  PUNCTUATION_TO_BRAILLE_MAPPINGS,
  CAPITAL_FOLLOWS_CASE,
  DECIMAL_FOLLOWS_CASE,
  NUMBER_FOLLOWS_CASE,
  SPACE_CASE,
} from "./translator-mappings.js";

function isNumber(char) {
  return !isNaN(Number(char));
}

function translateToBrailleChar(char, previous_char) {
  if (char === " ") {
    return SPACE_CASE;
  }

  if (previous_char !== " " && isNumber(previous_char)) {
    return NUMBERS_TO_BRAILLE_MAPPINGS.get(char);
  }

  if (char === char.toUpperCase() && char !== char.toLowerCase()) {
    return CAPITAL_FOLLOWS_CASE + ENGLISH_TO_BRAILLE_MAPPINGS.get(char.toLowerCase());
  }

  if (char !== " " && isNumber(char)) {
    return NUMBER_FOLLOWS_CASE + NUMBERS_TO_BRAILLE_MAPPINGS.get(char);
  }

  if (PUNCTUATION_TO_BRAILLE_MAPPINGS.has(char)) {
    return PUNCTUATION_TO_BRAILLE_MAPPINGS.get(char);
  }

  return ENGLISH_TO_BRAILLE_MAPPINGS.get(char.toLowerCase());
}

export default function translateToBraille(text) {
  let translateToBrailleArray = [];
  let previous_char = " ";

  for (let i = 0; i < text.length; i++) {
    translateToBrailleArray.push(translateToBrailleChar(text[i], previous_char));
    previous_char = text[i];
  }

  return translateToBrailleArray.join("");
}
