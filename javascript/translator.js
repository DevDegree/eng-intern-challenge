import translateToBraille from "./translation-to-braille.js";
import translateToEnglish from "./translation-to-english.js";

function isTextBraille(text) {
  let brailleCharacters = ["O", "."];

  for (const char of text) {
    if (!brailleCharacters.includes(char)) {
      return false;
    }
  }

  return true;
}

function translate(text) {
  if (!isTextBraille(text)) {
    return translateToBraille(text);
  }

  return translateToEnglish(text);
}

function main() {
  let textToBeTranslated = process.argv.slice(2).join(" ");
  console.log(translate(textToBeTranslated));
}

main();
