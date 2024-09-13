import {
  ENGLISH_TO_BRAILLE,
  ENGLISH_TO_NUMBERS,
  ENGLISH_SPACE,
  BRAILLE_TO_ENGLISH,
  BRAILLE_TO_NUMBERS,
  BRAILLE_SPACE,
  BRAILLE_CAPITAL,
  BRAILLE_NUMBER,
  BRAILLE_PREFIXES
} from "./constants";

function translateEnglishToBraille(englishText: string): string {
  let brailleText: string = "";
  let numberMode: boolean = false;

  for (const char of englishText) {
    const isNumber = !Number.isNaN(parseInt(char));
    brailleText += translateEnglishCharacterToBraille(char, numberMode, isNumber);
    numberMode = isNumber;
  }

  return brailleText;
}

function translateEnglishCharacterToBraille(char: string, numberMode: boolean, isNumber: boolean): string {
  const prefix: string = getBraillePrefix(char, numberMode, isNumber);

  if (char == ENGLISH_SPACE) return ENGLISH_TO_BRAILLE[char];
  if (isNumber) return prefix + ENGLISH_TO_NUMBERS[char]

  return prefix + ENGLISH_TO_BRAILLE[char.toLowerCase()];
}

function getBraillePrefix(char: string, numberMode: boolean, isNumber: boolean) {
  const isUpperCase: boolean = char === char.toUpperCase();

  if (isNumber && !numberMode) return BRAILLE_NUMBER;
  if (!isNumber && isUpperCase) return BRAILLE_CAPITAL;
  
  return "";
}

function translateBrailleToEnglish(brailleText: string): string {
  let englishText: string = "";
  let capitalMode: boolean = false;
  let numberMode: boolean = false;

  const brailleSymbols: string[] = splitBrailleIntoSymbols(brailleText);

  for (const symbol of brailleSymbols) {
    englishText += translateBrailleSymbolToEnglish(symbol, capitalMode, numberMode);

    if (symbol == BRAILLE_SPACE) numberMode = false;
    if (symbol == BRAILLE_NUMBER) numberMode = true;
    capitalMode = symbol == BRAILLE_CAPITAL;
  }

  return englishText;
}

const splitBrailleIntoSymbols = (braille: string): string[] => braille.match(/.{1,6}/g) || [];

function translateBrailleSymbolToEnglish(symbol: string, capitalMode: boolean, numberMode: boolean): string {
  const englishChar = BRAILLE_TO_ENGLISH[symbol];

  if (symbol == BRAILLE_SPACE) return ENGLISH_SPACE;
  if (numberMode) return BRAILLE_TO_NUMBERS[symbol];
  if (capitalMode) return englishChar.toUpperCase();
  if (!englishChar || BRAILLE_PREFIXES.includes(symbol)) return "";

  return capitalMode ? englishChar.toUpperCase() : englishChar;
}

const isValidBraille = (text: string): boolean => /^[O.]+$/.test(text) && text.length % 6 === 0;

const isValidEnglish = (text: string) => /^[a-zA-Z0-9 ]+$/.test(text);

function translate(text: string) {
  if (isValidBraille(text)) return translateBrailleToEnglish(text);
  if (isValidEnglish(text)) return translateEnglishToBraille(text);
}

function main() {
  const text: string = process.argv.slice(2).join(" ");
  const translation = translate(text) || "";
  console.log(translation);
}

main();
