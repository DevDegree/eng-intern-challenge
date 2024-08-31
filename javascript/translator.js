//First we need to map out which English Character is Braile
const englishToBraille = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
    ' ': '......',
    'capitalize': '.....O', 'number': '.O.OOO'
  };

  //We can reverse map this from Braile to English
  const brailleToEnglish = Object.fromEntries(
    Object.entries(englishToBraille).map(([key, value]) => [value, key])
  );

  function isBraille(input) {
    // RegEX to check if function is only braile by looking only for "O" and "."
    return /^[O.]+$/.test(input);
  }

  //Translates the English to Braile
  function translateEnglishToBraille(input) {
    let output = '';
    let isNumberMode = false;
    
    //for loop to iterate through each character and break it down to braile
    for (let i = 0; i < input.length; i++) {
      const char = input[i].toLowerCase();
  
      if (char === ' ') {
        isNumberMode = false;
        output += englishToBraille[char];
      } else if (char >= '0' && char <= '9') {
        if (!isNumberMode) {
          output += englishToBraille['number'];
          isNumberMode = true;
        }
        output += englishToBraille[char];
      } else {
        if (isNumberMode) {
          isNumberMode = false;
        }
        if (char >= 'a' && char <= 'z' && input[i] === input[i].toUpperCase()) {
          output += englishToBraille['capitalize'];
        }
        output += englishToBraille[char];
      }
    }
  
    return output;
  }

  //Opposite of the previous function
  function translateBrailleToEnglish(input) {
    let output = '';
    let isNumberMode = false;
    let isCapitalizeNext = false;
    
    for (let i = 0; i < input.length; i += 6) {
      const brailleChar = input.slice(i, i + 6);
  
      if (brailleChar === englishToBraille['capitalize']) {
        isCapitalizeNext = true;
      } else if (brailleChar === englishToBraille['number']) {
        isNumberMode = true;
      } else {
        let char = brailleToEnglish[brailleChar] || '';
        if (isCapitalizeNext && !isNumberMode) {
          char = char.toUpperCase();
          isCapitalizeNext = false;
        }
        output += char;
  
        if (char === ' ') {
          isNumberMode = false;
        }
      }
    }
  
    return output;
  }

  function translate(input) {
    if (isBraille(input)) {
      return translateBrailleToEnglish(input);
    } else {
      return translateEnglishToBraille(input);
    }
  }

  if (require.main === module) {
    const input = process.argv.slice(2).join(' ');
    console.log(translate(input));
  }