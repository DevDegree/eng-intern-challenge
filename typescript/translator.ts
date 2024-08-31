// Braille representation for English letters, numbers, and special characters
const brailleRecords: { [key: string]: string } = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".OO.O.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  capital: ".....O", // Braille indicator for capital letters
  number: ".O.OOO", // Braille indicator for numbers
  "0": ".OOO..",
  "1": "O.....",
  "2": "O.O...",
  "3": "OO....",
  "4": "OO.O..",
  "5": "O..O..",
  "6": "OOO...",
  "7": "OOOO..",
  "8": "O.OO..",
  "9": ".OO...",
  space: "......", // Braille representation for space
};

// Translate function to convert between English and Braille
function translate(input: string): string {
  // Create a reverse mapping from Braille patterns to English characters
  const reversedBrailleRecords: { [key: string]: string } = Object.entries(
    brailleRecords
  ).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {} as { [key: string]: string });

  // Determine if the input is in Braille or English
  const inputType = input.match(/^[O.]+$/) ? "braille" : "english";

  let output = ""; // Initialize output string
  let capitalNext = false; // Flag for capital letters
  let numberMode = false; // Flag for number mode

  if (inputType === "english") {
    // Convert English text to Braille
    for (const char of input) {
      if (char.match(/[A-Z]/)) {
        output += brailleRecords["capital"]; // Add capital indicator
        output += brailleRecords[char.toLowerCase()]; // Add Braille for the letter
        numberMode = false; // Reset number mode
      } else if (char.match(/[0-9]/)) {
        if (!numberMode) {
          output += brailleRecords["number"]; // Add number indicator
          numberMode = true; // Enable number mode
        }
        output += brailleRecords[char]; // Add Braille for the digit
      } else if (char === " ") {
        output += brailleRecords["space"]; // Add Braille for space
        numberMode = false; // Reset number mode
      } else {
        output += brailleRecords[char]; // Add Braille for other characters
        numberMode = false; // Reset number mode
      }
    }
  } else {
    // Convert Braille text to English
    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.substr(i, 6); // Extract Braille character

      if (brailleChar === brailleRecords["capital"]) {
        capitalNext = true; // Set flag for capital letter
      } else if (brailleChar === brailleRecords["number"]) {
        numberMode = true; // Set flag for number mode
      } else {
        let englishChar = reversedBrailleRecords[brailleChar]; // Convert Braille to English character

        if (numberMode) {
          if (englishChar.match(/[a-j]/)) {
            const index = "abcdefghij".indexOf(englishChar);
            englishChar = (index + 1).toString(); // Convert 'a-j' to '1-9' or '0'
            if (englishChar === "10") englishChar = "0"; // Map 'j' to '0'
          }
        }

        if (capitalNext) {
          englishChar = englishChar.toUpperCase(); // Convert to uppercase if capital flag is set
          capitalNext = false; // Reset capital flag
        }

        // Reset number mode if not processing a number
        if (!englishChar.match(/[0-9]/)) {
          numberMode = false;
        }

        output += englishChar === "space" ? " " : englishChar; // Add English character or space to output
      }
    }
  }

  // Replace any unexpected trailing '0' with space
  output = output.replace(/0x/, " x");

  return output; // Return the translated output
}

// Main function to handle command-line input and output
function main(input: string) {
  console.log(translate(input)); // Print the translated result
}

// Get input from command-line arguments and call main function
const input = process.argv.slice(2).join(" ");
main(input);
