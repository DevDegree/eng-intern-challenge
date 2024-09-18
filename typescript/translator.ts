import { argv } from "process";
import {
  brailleToEnglishMap,
  brailleToNumberMap,
  englishToBrailleMap,
  brailleInputRegex,
  numbersToBrailleMap,
  isNumeric
} from "./translatorUtils";

// ignore first two args, node location and file path
const args = argv.slice(2);

function translateBrailleToText(brailleInput: string): string {
  // match splits into 6 char chunks, already validated by regex
  const brailleChars = brailleInput.match(/.{1,6}/g) || [];
  let result = "";
  let isNumber = false;

  for (let i = 0; i < brailleChars.length; i++) {
    const char = brailleToEnglishMap.get(brailleChars[i]);
    switch (char) {
      case "capital":
        result += brailleToEnglishMap.get(brailleChars[++i])?.toUpperCase();
        break;
      case "number":
        isNumber = true;
        break;
      case " ":
        result += char;
        isNumber = false;
        break;
      default:
        if (isNumber) {
          result += brailleToNumberMap.get(brailleChars[i]) || "";
        } else {
          result += char || "";
        }
        break;
    }
  }

  return result;
}

function translateTextToBraille(textInput: string[]): string {
  const result: string[] = [];
  // bool flag simplifies logic, numbers must be followed by space, otherwise interpreted as letter
  let isNumber = false;

  for (const string of textInput) {
    for (const char of string) {
      if (isNumber && numbersToBrailleMap.has(char)) {
        result.push(numbersToBrailleMap.get(char)!);
      } else if (isNumeric(char)) {
        isNumber = true;
        result.push(englishToBrailleMap.get("number")!);
        result.push(numbersToBrailleMap.get(char)!);
      } else if (char === char.toUpperCase() && char !== " ") {
        result.push(englishToBrailleMap.get("capital")!);
        result.push(englishToBrailleMap.get(char.toLowerCase())!);
      } else {
        result.push(englishToBrailleMap.get(char)!);
      }
    }
    result.push(englishToBrailleMap.get(" ")!);
    isNumber = false;
  }

  return result.join("").slice(0, -6); // Remove the last space
}

if (args.length === 1 && brailleInputRegex.test(args[0])) {
  console.log(translateBrailleToText(args[0]));
} else {
  console.log(translateTextToBraille(args));
}
