import {
  brailleAlphabetMapping,
  BrailleKey,
  brailleNumberMapping,
  englishAlphabetMapping,
  EnglishKey,
  englishNumberMapping,
} from "./constants";

function main() {
  try {
    // Parse command-line arguments
    const textToTranslate = process.argv.slice(2).join(" ");

    if (textToTranslate.length === 0)
      throw new Error("No text provided to translate");

    // Detect if braille or english
    const isBraille = new RegExp(/^[.O]+$/);
    if (isBraille.test(textToTranslate))
      return brailleToEnglish(textToTranslate);
    else return englishToBraille(textToTranslate);
  } catch (error: unknown) {
    console.log(error);
  }
}

const chunkedBraille: string[] = [];

function brailleToEnglish(text: string) {
  // Chunk up the braille input into 6 letter strings
  for (let i = 0; i < text.length; i += 6) {
    chunkedBraille.push(text.slice(i, i + 6));
  }

  let englishResult = "";
  let i = 0;

  // Iterate through all of the chunked braille
  while (i < chunkedBraille.length) {
    const brailleString = chunkedBraille[i] as BrailleKey;

    if (!(brailleString in brailleAlphabetMapping))
      throw new Error(`Invalid Braille character ${brailleString}`);

    const englishCharacter = brailleAlphabetMapping[brailleString];

    // Number follows retrieve characters from the number
    if (englishCharacter === "nf") {
      i += 1; //Skip adding the 'nf' character

      // Loop over all of the braille numbers until you reach a space
      while (i < chunkedBraille.length) {
        const numberCharacter = getMappedBraille(
          i,
          brailleNumberMapping,
          "Invalid braille number mapping"
        );
        englishResult += numberCharacter;

        if (numberCharacter === " ") break; //Break once we reach a space (stated in requirements: 'assume all following symbols are numbers until the next space symbol.')
        i += 1;
      }
    }
    // Check for if a capital letter follows or a decimal follows
    else if (englishCharacter === "cf" || englishCharacter === "df") {
      i += 1; //Skip adding the 'cf' character

      const uncapitalizedCharacter = getMappedBraille(
        i,
        brailleAlphabetMapping,
        "Invalid Capital Alphabet Character"
      );
      englishResult += uncapitalizedCharacter!.toUpperCase();
    }
    // Add the letter to the string
    else {
      // Add alphabetical character to result
      englishResult += englishCharacter;
    }
    i += 1;
  }

  return englishResult;
}

/**
 * Returns back the corresponding braille string based on passed in braille hashmap.
 */
function getMappedBraille(
  idx: number,
  brailleMapping: Partial<Record<BrailleKey, string>>,
  errorMsg: string
) {
  if (idx >= chunkedBraille.length) return "";

  const brailleString = chunkedBraille[idx] as BrailleKey;

  if (!(brailleString in brailleMapping))
    throw new Error(`${errorMsg} ${brailleString}`);

  return brailleMapping[brailleString];
}

function englishToBraille(text: string) {
  let brailleResult = "";
  let i = 0
  while (i < text.length) {
    if (/^[0-9]$/.test(text[i])) {
      brailleResult += englishAlphabetMapping["nf"];

      // Iterate until we reach a non-digit character 
      while (/^[0-9]$/.test(text[i]) && i < text.length) {
        brailleResult += englishNumberMapping[text[i] as EnglishKey];
        i += 1;
      }
      continue;
    } else if (text[i] === ".") {

      // Add the delimiter decimal follows character and the following decimal character
      brailleResult += englishAlphabetMapping["df"];
      brailleResult += englishAlphabetMapping[text[i] as EnglishKey];
    } else if (/^[A-Z]$/.test(text[i])) {

      // 
      brailleResult += englishAlphabetMapping["cf"];
      brailleResult +=
        englishAlphabetMapping[text[i].toLowerCase() as EnglishKey];
    } else {

      //
      brailleResult += englishAlphabetMapping[text[i] as EnglishKey];
    }

    i +=1
  }

  return brailleResult;
}

console.log(main());
