const brailleMap = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......', '0': '.OOO..', '1': 'O.....', '2': 'O.O...',
    '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', 
    '8': 'O.OO..', '9': '.OO...'
  };
  
  const numSymbol = '.O.OOO';
  const capSymbol = '.....O';
  
  const reverseBrailleMap = Object.fromEntries(
    Object.entries(brailleMap).map(([char, braille]) => [braille, char])
  );
  
  const decodeBraille = (brailleInput) => {
    const brailleLength = 6;
    let result = "";
    let isCapital = false;
    let isNumber = false;
  
    for (let i = 0; i < brailleInput.length; i += brailleLength) {
      const braillePattern = brailleInput.substring(i, i + brailleLength);
  
      if (braillePattern === capSymbol) {
        isCapital = true;
        continue;
      } else if (braillePattern === numSymbol) {
        isNumber = true;
        continue;
      } else if (braillePattern === "......") {
        isNumber = false;
        result += " ";
        continue;
      }
  
      let decodedChar = reverseBrailleMap[braillePattern] || "?";
  
      if (isNumber) {
        if (decodedChar >= 'a' && decodedChar <= 'i') {
          decodedChar = String.fromCharCode(decodedChar.charCodeAt(0) - 'a'.charCodeAt(0) + '1'.charCodeAt(0));
        } else if (decodedChar === 'j') {
          decodedChar = '0';
        }
        result += decodedChar; 
      } else if (isCapital && decodedChar !== ' ') {
        decodedChar = decodedChar.toUpperCase();
        isCapital = false;
        result += decodedChar;
      } else {
        result += decodedChar;
      }
    }
  
    return result;
  };
  
  const encodeEnglish = (englishInput) => {
    let result = "";
    let inNumberSequence = false;
  
    for (const char of englishInput) {
      if (char === " ") {
        result += "......";
        inNumberSequence = false;
      } else if (char >= "A" && char <= "Z") {
        result += ".....O";
        result += brailleMap[char.toLowerCase()] || "......";
        inNumberSequence = false;
      } else if (char >= "0" && char <= "9") {
        if (!inNumberSequence) {
          result += numSymbol; 
          inNumberSequence = true;
        }
        result += brailleMap[char];
      } else {
        result += brailleMap[char] || "......";
        inNumberSequence = false;
      }
    }
  
    return result;
  };
  
  const processInput = (input) => {
    const isDivisibleBy6 = input.length % 6 === 0;
    const containsBrailleCharacters = /[O.]/.test(input);
  
    if (isDivisibleBy6 && containsBrailleCharacters) {
      return decodeBraille(input);
    } else {
      return encodeEnglish(input);
    }
  };
  
  const args = process.argv.slice(2);
  const input = args.join(" ");
  
  console.log(processInput(input));