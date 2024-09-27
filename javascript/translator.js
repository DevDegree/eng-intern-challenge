// Braille symbols for letters, numbers, capital follows, and number follows
const brailleMap = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
  'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
  'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
  'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
  'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
  'z': 'O..OOO', ' ': '......', // Space
  // Special symbols
  'capital': '.....O', // Capital follows
  'number': '.O.OOO',  // Number follows
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
  '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
};


//Reverse mapping for ENGLISH TO BRAILLE
const reverseBrailleMap = Object.entries(brailleMap).reduce(
  (obj, [key, value]) => {
    obj[value] = key;
    return obj;
  },
  {}
);

//Defining function to translate input to BRAILLE
const translateToBraille = (input) => {
  let result = '';
  let inNumbersMode = false;
  
  for (let char of input) {
    if (char >= 'A' && char <= 'Z') {
      result += brailleMap['capital'];  // Add capital follows symbol
      char = char.toLowerCase();
    }
    if (char >= '0' && char <= '9') {
      if (!inNumbersMode) {
        result += brailleMap['number'];  // Add number follows symbol
        inNumbersMode = true;
      }
      result += brailleMap[char];
    } else {
      inNumbersMode = false;
      result += brailleMap[char] || ''; // Lookup in the map
    }
  }
  return result;
}

//Defining function to translate to ENGLISH
const translateToEnglish = (braille) => {
  let result = '';
  let inCapitalizeMode = false;
  let inNumbersMode = false;

  for (let i = 0; i < braille.length; i += 6) {
    const symbol = braille.slice(i, i + 6);

    if (symbol === brailleMap['capital']) {
      inCapitalizeMode = true;
      continue;
    }

    if (symbol === brailleMap['number']) {
      inNumbersMode = true;
      continue;
    }

    let letter = reverseBrailleMap[symbol];

    if (inCapitalizeMode && letter) {
      letter = letter.toUpperCase();
      inCapitalizeMode = false;
    }

    if (inNumbersMode && letter) {
      inNumbersMode = false;
    }

    result += letter || '';
  }
  return result;
}

//Main funtion to handle the translation
const translate = (input) => {
  if (input.match(/^[O.]+$/)) {
    return translateToEnglish(input);
  } else {
    return translateToBraille(input);
  }
}

//Command-Line input
const input = process.argv.slice(2).join(" ");
console.log(translate(input));
