const brailleToEnglish = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d",
    "O..O..": "e", "OOO...": "f", "OOOO..": "g", "O.OO..": "h",
    ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p",
    "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z",
    ".....O": "capital", ".O.OO.": "number",
    "......": " ",
  };
  
  const englishToBraille = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..",
    "e": "O..O..", "f": "OOO...", "g": "OOOO..", "h": "O.OO..",
    "i": ".OO...", "j": ".OOO..", "k": "O...O.", "l": "O.O.O.",
    "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.", "p": "OOO.O.",
    "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO",
    "y": "OO.OOO", "z": "O..OOO",
    "A": ".....OO.....", "B": ".....OO.O...", "C": ".....OOO....",
    "D": ".....OOO.O..", "E": ".....OO..O..", "F": ".....OOOO...",
    "G": ".....OOOO.", "H": ".....OO.OO..", "I": ".....O.OO...",
    "J": ".....O.OOO..", "K": ".....OO...O.", "L": ".....OO.O.O.",
    "M": ".....OOO..O.", "N": ".....OOO.OO.", "O": ".....OO..OO.",
    "P": ".....OOOO.O.", "Q": ".....OOOOOO.", "R": ".....OO.OOO.",
    "S": ".....O.OO.O.", "T": ".....O.OOOO.", "U": ".....OO...OO",
    "V": ".....OO.O.OO", "W": ".....O.OOO.O", "X": ".....OOO..OO",
    "Y": ".....OOO.OOO", "Z": ".....OO..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....",
    "4": "OO.O..", "5": "O..O..", "6": "OOO...",
    "7": "OOOO..", "8": "O.OO..", "9": ".OO...",
    "0": ".OOO..", " ": "......",
  };
  
  function isBrailleText(input) {
    return /^[O.]+$/.test(input);
  }
  
  function translateToEnglish(braille) {
    const words = braille.trim().split("......");
    let result = "";
    let isCapital = false;
    let isNumber = false;
  
    words.forEach(word => {
      const chars = word.match(/.{1,6}/g) || [];
      chars.forEach(char => {
        const translatedChar = brailleToEnglish[char] || "";
  
        if (translatedChar === "capital") {
          isCapital = true;
        } else if (translatedChar === "number") {
          isNumber = true;
        } else if (translatedChar === " ") {
          result += " ";
          isCapital = false;
          isNumber = false;
        } else {
          if (isCapital) {
            result += translatedChar.toUpperCase();
            isCapital = false;
          } else if (isNumber) {
            result += translatedChar;
          } else {
            result += translatedChar;
          }
        }
      });
      result += " ";
    });
  
    return result.trim();
  }
  
  function translateToBraille(englishText) {
    let result = "";
    let isInNumberSequence = false;

    for (let i = 0; i < englishText.length; i++) {
      const char = englishText[i];
      
      if (/[0-9]/.test(char)) {
        if (!isInNumberSequence) {
          result += ".O.OOO"; // Add number indicator only at the start of a number sequence
          isInNumberSequence = true;
        }
        result += englishToBraille[char];
      } else {
        isInNumberSequence = false;
        result += englishToBraille[char] || "";
      }
    }

    return result;
  }
  
  function translate(input) {
    if (isBrailleText(input)) {
      return translateToEnglish(input);
    } else {
      return translateToBraille(input);
    }
  }
  
  function main() {
    const args = process.argv.slice(2);
    const input = args.join(" ");

    if (!input) {
      console.error("Please provide input to translate.");
      process.exit(1);
    }
  
    const translated = translate(input);
    console.log(translated);
  }
  
  main();