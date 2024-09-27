const alphabet = require('./alphabet');

const brailleCharacters = alphabet.brailleCharacters;
const brailleNumbers = alphabet.brailleNumbers;

const englishCharacters = alphabet.englishCharacters;
const englishNumbers = alphabet.englishNumbers;

const args = process.argv.slice(2).join(" ");

// Determine if input is English or Braille
function isBraile(args) {
  const braileChar = [".", "O"];
  const charArray = args.split("");
  let bool = true;

  charArray.forEach((char) => {
    if (braileChar.includes(char)) {
      bool = true;
    } else {
      bool = false;
    }
  });
  return bool;
}

// Convert English to Braille
function toBraille(englishText) {
  let result = "";
  let numberMode = false;

  for (let i = 0; i < englishText.length; i++) {
    const char = englishText[i];

    // Uppercase letters
    if (char >= "A" && char <= "Z") {
      result += brailleCharacters.capitalFollows + brailleCharacters[char];
    // Lowercase letters
    } else if (char >= "a" && char <= "z") {
      result += brailleCharacters[char.toUpperCase()];
    // Numbers
    } else if (char >= "0" && char <= "9") {
      if (!numberMode) {
        result += brailleCharacters.numberFollows;
        numberMode = true;
      }
      result += brailleNumbers[char];
    // Space character
    } else if (char === " ") {
      result += brailleCharacters.space;
      numberMode = false;
    // Unmapped characters
    } else {
      result += "[Unmapped]";
    }
  }

  return result;
}

// Convert Braille to English
function toEnglish(brailleText) {
  let result = "";
  let index = 0;
  let capitalMode = false;
  let numberMode = false;

  while (index < brailleText.length) {
    const brailleChar = brailleText.slice(index, index + 6);

    if (brailleChar === brailleCharacters.capitalFollows) {
      capitalMode = true;
      index += 6;
      continue;
    }

    if (brailleChar === brailleCharacters.numberFollows) {
      numberMode = true;
      index += 6;
      continue;
    }

    if (brailleChar === brailleCharacters.space) {
      result += " ";
      numberMode = false;
      index += 6;
      continue;
    }
    
    let char =
      numberMode === true
        ? englishNumbers[brailleChar]
        : englishCharacters[brailleChar];

    // Numbers    
    if (numberMode && char >= "1" && char <= "9") {
      result += char;
    // Space character
    } else if (numberMode && char == "space") {
      result += char;
      numberMode = false;
    // Uppercase letters
    } else if (capitalMode && char >= "A" && char <= "Z") {
      result += char;
      capitalMode = false;
      numberMode = false;
    // Lowercase letter and Unmapped characters
    } else {
      result += char?.toLowerCase() || "[Unmapped]";
    }

    index += 6;
  }
  return result;
}

if (isBraile(args)) {
  // toEnglish
  console.log(toEnglish(args));
} else {
  // toBraile
  console.log(toBraille(args));
}