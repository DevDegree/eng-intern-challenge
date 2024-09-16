const {
  ENGLISH_TO_BRAILLE_MAP,
  BRAILLE_TO_ENGLISH_MAP,
  capitalIndicator,
  numberIndicator,
} = require("./brailleMaps");

// Convert English text to Braille
function englishToBraille(text) {
  let brailleText = "";
  let isNumber = false; // Track if we are in number mode due to preceding number indicator

  for (const char of text) {
    if (char === " ") {
      brailleText += ENGLISH_TO_BRAILLE_MAP[" "]; // Add Braille space
      isNumber = false; // Exit number mode on space
    } else if (char >= "A" && char <= "Z") {
      brailleText +=
        capitalIndicator + ENGLISH_TO_BRAILLE_MAP[char.toLowerCase()];
      isNumber = false; // Exit number mode on letter
    } else if (char >= "0" && char <= "9") {
      if (!isNumber) {
        brailleText += numberIndicator; // Add number indicator if not already in number mode
        isNumber = true;
      }
      brailleText += ENGLISH_TO_BRAILLE_MAP[char];
    } else {
      brailleText += ENGLISH_TO_BRAILLE_MAP[char] || ""; // Add Braille for other characters
      isNumber = false; // Exit number mode if character is not a number
    }
  }

  return brailleText;
}

// Convert Braille text to English
function brailleToEnglish(brailleText) {
  let result = "";
  let isCapital = false;
  let isNumber = false;

  for (let i = 0; i < brailleText.length; i += 6) {
    const brailleChar = brailleText.slice(i, i + 6);

    if (brailleChar === capitalIndicator) {
      isCapital = true;
    } else if (brailleChar === numberIndicator) {
      isNumber = true;
    } else {
      const char = BRAILLE_TO_ENGLISH_MAP[brailleChar] || "";

      if (isNumber) {
        if (char >= "a" && char <= "j") {
          // Convert Braille letters 'a' to 'j' to digits '1' to '0' when in number mode
          result += (char.charCodeAt(0) - "a".charCodeAt(0) + 1) % 10;
        } else if (char === " ") {
          // If a space is encountered, exit number mode
          result += char;
          isNumber = false;
        }
      } else {
        result += isCapital ? char.toUpperCase() : char;
        isCapital = false; // Reset capital flag after use
      }
    }
  }

  return result;
}

// Command-line input handling
const [, , ...args] = process.argv;
const input = args.join(" ");

if (input.trim() === "") {
  console.log("Input is empty or only contains spaces.");
} else if (input.match(/^[.O\s]+$/)) {
  // Input seems to be Braille
  console.log(brailleToEnglish(input.replace(/\s+/g, "")));
} else {
  // Input seems to be English
  console.log(englishToBraille(input));
}
