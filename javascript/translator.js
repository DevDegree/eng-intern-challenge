const brailleAlphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",
    "capital": ".....O",
    "number": ".O.OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
  };
  
  const brailleToEnglish = Object.entries(brailleAlphabet).reduce((acc, [key, value]) => {
    acc[value] = key;
    return acc;
  }, {});
  
  function isBraille(input) {
    return /^[O.]+$/.test(input);
  }
  
  function englishToBraille(text) {
    let result = '';
    let numberMode = false;
    for (let char of text) {
      if (/[A-Z]/.test(char)) {
        result += brailleAlphabet['capital'];
        char = char.toLowerCase();
      }
      if (/[0-9]/.test(char) && !numberMode) {
        result += brailleAlphabet['number'];
        numberMode = true;
      }
      if (char === ' ' || !/[0-9]/.test(char)) {
        numberMode = false;
      }
      result += brailleAlphabet[char] || '';
    }
    return result;
  }
  
  function brailleToEnglishConversion(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
    for (let i = 0; i < braille.length; i += 6) {
      const brailleChar = braille.slice(i, i + 6);
      if (brailleChar === brailleAlphabet['capital']) {
        isCapital = true;
        continue;
      }
      if (brailleChar === brailleAlphabet['number']) {
        isNumber = true;
        continue;
      }
      let translatedChar = brailleToEnglish[brailleChar];
      if (isCapital && translatedChar) {
        translatedChar = translatedChar.toUpperCase();
        isCapital = false;
      }
      if (isNumber && translatedChar) {
        isNumber = false;
      }
      result += translatedChar || '';
    }
    return result;
  }
  
  function translate(input) {
    return isBraille(input) ? brailleToEnglishConversion(input) : englishToBraille(input);
  }
  
  const args = process.argv.slice(2).join(' ');
  if (args) {
    console.log(translate(args));
  }
  