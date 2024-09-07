import fs from "fs";
const engToBraille = JSON.parse(fs.readFileSync("engToBraille.json", "utf-8"));
const brailleToEngLetters = JSON.parse(
  fs.readFileSync("./brailleToEngLetters.json", "utf-8")
);
const brailleToEngNumbers = JSON.parse(
  fs.readFileSync("./brailleToEngNumbers.json", "utf-8")
);

function convertEnglishToBraille(input) {
  let brailleOutput = "";
  let numberMode = false;

  for (let i = 0; i < input.length; i++) {
    const character = input[i];

    // if character is capital, then add braille for capitalization
    if (character === character.toUpperCase() && isNaN(character)) {
      brailleOutput += engToBraille["capital"];
    }

    // if character is number and we're not already in number mode, then add braille delim for numbers START
    if (!isNaN(character) && character !== " " && !numberMode) {
      brailleOutput += engToBraille["number"];
      numberMode = true;
    }
    // if character is not number and character is not space and numberMode is ON, add the braille delim for numbers END
    else if (isNaN(character) && character !== " " && numberMode) {
      brailleOutput += engToBraille[" "];
      numberMode = false;
      // if character is space and numberMode is ON, skip the character conversion
    } else if (character === " " && numberMode) {
      brailleOutput += engToBraille[" "];
      numberMode = false;
      continue;
    }

    let braille = engToBraille[character.toLowerCase()];
    // console.log("character:", character, "braile:", braille);
    brailleOutput += braille;
  }

  return brailleOutput;
}

function convertBrailleToEnglish(input) {
  let englishOutput = "";
  let numberMode = false;
  let capitalMode = false;

  for (let i = 0; i < input.length; i += 6) {
    const brailleChar = input.slice(i, i + 6);

    // check for number START delim
    if (brailleChar === engToBraille["number"]) {
      numberMode = true;
      continue;
    }

    // check for capital delim
    if (brailleChar === engToBraille["capital"]) {
      capitalMode = true;
      continue;
    }

    // check for space (number END) delim
    if (brailleChar === engToBraille[" "]) {
      if (numberMode) {
        numberMode = false;
      }
      englishOutput += " ";
      continue;
    }

    let translatedChar = "";
    if (numberMode) {
      translatedChar = brailleToEngNumbers[brailleChar];
    } else {
      translatedChar = brailleToEngLetters[brailleChar];
      if (capitalMode && translatedChar) {
        translatedChar = translatedChar.toUpperCase();
        capitalMode = false;
      }
    }

    if (translatedChar) {
      englishOutput += translatedChar;
    }
  }

  return englishOutput;
}

function isBraille(characters) {
  for (let i = 0; i < characters.length; i++) {
    const character = characters[i];

    if (character === "O" || character === ".") {
      continue;
    } else {
      return false;
    }
  }
  return true;
}

let result = "";
const args = process.argv.slice(2);
const input = args.join(" ");

if (isBraille(input)) {
  result = convertBrailleToEnglish(input);
} else {
  result = convertEnglishToBraille(input);
}
console.log(result);
