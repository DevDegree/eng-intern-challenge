// Define combined Braille mappings and special symbols
const brailleMap = {
    // Braille mappings for letters and punctuation
    a: "O.....", b: "O.O...", c: "OO....", d: "OO.O..", e: "O..O..",
    f: "OOO...", g: "OOOO..", h: "O.OO..", i: ".OO...", j: ".OOO..",
    k: "O...O.", l: "O.O.O.", m: "OO..O.", n: "OO.OO.", o: "O..OO.",
    p: "OOO.O.", q: "OOOOO.", r: "O.OOO.", s: ".OO.O.", t: ".OOOO.",
    u: "O...OO", v: "O.O.OO", w: ".OOO.O", x: "OO..OO", y: "OO.OOO", z: "O..OOO",
    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.", ":": "..OO..",
    ";": "..O.O.", "-": "....OO", "/": ".O..O.", "<": ".OO..O",
    ">": "O.0OO.", "(": "O.O..O", ")": ".O.OO.", " ": "......",
  
    // Special symbols for Braille
    "capitalize": ".....O", // Capital follows
    "number": ".O.OOO",     // Number follows
    "decimal": ".O...O",    // Decimal follows
  };
  
  // Define Braille mappings for numbers
  const brailleNumberMap = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..",
  };
  
  // Reverse Braille maps
  const reverseBrailleMap = Object.entries(brailleMap).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {});
  
  const reverseBrailleNumberMap = Object.entries(brailleNumberMap).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {});
  
  // Detect if input is Braille or English
  function isBraille(input) {
    return input.includes("O") || input.includes(".");
  }
  
  // Translate English to Braille
  function englishToBraille(text) {
    let result = "";
    let isCapital = false;
    let isNumber = false;
  
    console.log("English to Braille conversion:");
  
    for (let char of text) {
      console.log(`Processing character: ${char}`);
  
      if (char >= 'A' && char <= 'Z') {
        if (!isCapital) {
          result += brailleMap["capitalize"];
          isCapital = true;
          console.log(`Adding capitalization symbol: ${brailleMap["capitalize"]}`);
        }
        char = char.toLowerCase();
      } else if (char >= '0' && char <= '9') {
        if (!isNumber) {
          result += brailleMap["number"];
          isNumber = true;
          console.log(`Adding number symbol: ${brailleMap["number"]}`);
        }
      } else {
        isNumber = false;
        isCapital = false;
      }
  
      const brailleChar = brailleMap[char] || "";
      result += brailleChar;
      console.log(`Mapped character: ${char} to Braille: ${brailleChar}`);
    }
  
    return result;
  }
  
  // Translate Braille to English
  function brailleToEnglish(braille) {
    let result = "";
    let i = 0;
    let isCapital = false;
    let isNumberMode = false;

    console.log("Braille to English conversion:");

    while (i < braille.length) {
        const symbol = braille.slice(i, i + 6);

        console.log(`Processing symbol: ${symbol}`);

        if (symbol === brailleMap["capitalize"]) {
            isCapital = true;
            i += 6;
            console.log(`Found capitalization symbol.`);
            continue;
        }

        if (symbol === brailleMap["number"]) {
            isNumberMode = true;
            i += 6;
            console.log(`Found number symbol.`);
            continue;
        }

        if (symbol === brailleMap["decimal"]) {
            result += '.';
            i += 6;
            console.log(`Found decimal symbol.`);
            continue;
        }

        const letter = isNumberMode ? reverseBrailleNumberMap[symbol] : reverseBrailleMap[symbol];

        if (!letter) {
            console.log(`Unrecognized symbol: ${symbol}`);
            i += 6; // Move to the next symbol even if unrecognized
            continue;
        }

        if (isCapital) {
            result += letter.toUpperCase();
            isCapital = false;
            console.log(`Mapped Braille symbol: ${symbol} to capital letter: ${letter.toUpperCase()}`);
        } else if (isNumberMode && /^[0-9]$/.test(letter)) {
            result += letter;
            console.log(`Mapped Braille symbol: ${symbol} to number: ${letter}`);
        } else {
            result += letter;
            console.log(`Mapped Braille symbol: ${symbol} to letter: ${letter}`);
        }

        // Reset number mode after processing a number
        if (isNumberMode && /^[a-z]$/.test(letter)) {
            isNumberMode = false;
        }

        i += 6;
    }

    return result;
}

  // Main function
  function translate(input) {
    if (isBraille(input)) {
      return brailleToEnglish(input);
    } else {
      return englishToBraille(input);
    }
  }
  
  // CLI interaction
  const args = process.argv.slice(2);
  if (args.length > 0) {
    const input = args.join(" ");
    const output = translate(input);
    console.log(output);
  }
  