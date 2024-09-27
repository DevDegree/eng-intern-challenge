const brailleMap = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',
    'CAPITAL': '.....O',
    'NUMBER': '.O.OOO'
  };
  
  const numberMap = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
  };
  
  function englishToBraille(text) {
    let result = '';
    let isNumber = false;
  
    for (let char of text) {
      if (char.match(/[A-Z]/)) {
        result += brailleMap['CAPITAL'];
        char = char.toLowerCase();
      }
  
      if (char.match(/[0-9]/)) {
        if (!isNumber) {
          result += brailleMap['NUMBER'];
          isNumber = true;
        }
        result += numberMap[char];
      } else {
        isNumber = false;
        result += brailleMap[char.toLowerCase()] || '';
      }
    }
  
    return result;
  }
  
  function brailleToEnglish(braille) {
    let result = '';
    let isCapital = false;
    let isNumber = false;
  
    for (let i = 0; i < braille.length; i += 6) {
      const char = braille.slice(i, i + 6);
  
      if (char === brailleMap['CAPITAL']) {
        isCapital = true;
        continue;
      }
  
      if (char === brailleMap['NUMBER']) {
        isNumber = true;
        continue;
      }
  
      if (isNumber) {
        const num = Object.keys(numberMap).find(key => numberMap[key] === char);
        if (num) {
          result += num;
          continue;
        } else {
          isNumber = false;
        }
      }
  
      const letter = Object.keys(brailleMap).find(key => brailleMap[key] === char);
      if (letter) {
        result += isCapital ? letter.toUpperCase() : letter;
        isCapital = false;
      }
    }
  
    return result;
  }
  
  function translate(input) {
    if (input.match(/^[O.]+$/)) {
      return brailleToEnglish(input);
    } else {
      return englishToBraille(input);
    }
  }
  
  // Get input from command line arguments
  const input = process.argv.slice(2).join(' ');
  
  // Translate and output the result
  console.log(translate(input));
  