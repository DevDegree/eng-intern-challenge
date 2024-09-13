const englishToBraille = {
    a: 'O.....',
    b: 'O.O...',
    c: 'OO....',
    d: 'OO.O..',
    e: 'O..O..',
    f: 'OOO...',
    g: 'OOOO..',
    h: 'O.OO..',
    i: '.00...',
    j: '.OOO..',
    k: 'O...O.',
    l: 'O.O.O.',
    m: 'OO..O.',
    n: 'OO.OO.',
    o: 'O..OO.',
    p: 'OOO.O.',
    q: 'OOOOO.',
    r: 'O.OOO.',
    s: '.OO.O.',
    t: '.OOOO.',
    u: 'O...OO',
    v: 'O.O.OO',
    w: '.OOO.O',
    x: 'OO..OO',
    y: 'OO.OOO',
    z: 'O..OOO',
    ' ': '......',
    capitalFollows: '.....O',
  };
  
  const numberToBraille = {
    numberFollows: '.O.OOO',
    '0': '.OOO..',
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'OO.OOO',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
  };
  
  const brailleToEnglish = Object.fromEntries(
    Object.entries(englishToBraille).map(([key, value]) => [value, key])
  );
  
  const brailleToNumber = Object.fromEntries(
    Object.entries(numberToBraille).map(([key, value]) => [value, key])
  );
  
  const isUpperCase = (char) => char === char.toUpperCase();
  
  const translateEnglishToBraille = (text) => {
    let braille = '';
    let numberMode = false;
  
    for (let char of text) {
      if (numberMode && char === ' ') {
        numberMode = false;
      }
  
      if (!numberMode && /\d/.test(char)) {
        braille += numberToBraille.numberFollows;
        numberMode = true;
      }

      if (/[A-Z]/.test(char)) {
        braille += englishToBraille.capitalFollows;
        char = char.toLowerCase();
      }
  
      braille += (numberMode ? numberToBraille : englishToBraille)[char];
    }
  
    return braille;
  };
  
  const translateBrailleToEnglish = (braille) => {
    let text = '';
    let capitalize = false;
    let numberMode = false;
  
    for (let i = 0; i < braille.length; i += 6) {
      const char = braille.slice(i, i + 6);
  
      if (char === englishToBraille.capitalFollows) {
        capitalize = true;
        continue;
      }
  
      if (char === numberToBraille.numberFollows) {
        numberMode = true;
        continue;
      }
  
      if (numberMode && char === englishToBraille[' ']) {
        numberMode = false;
      }
  
      let translatedChar = (numberMode ? brailleToNumber : brailleToEnglish)[char];
  
      if (capitalize) {
        translatedChar = translatedChar.toUpperCase();
        capitalize = false;
      }
  
      text += translatedChar;
    }
  
    return text;
  };
  
  const translateBrailleOrEnglish = (input) => {
    if (/^[O.]+$/.test(input)) {
      return translateBrailleToEnglish(input);
    } else {
      return translateEnglishToBraille(input);
    }
  };
  

  const input = process.argv.slice(2).join(' ');
  
  console.log(translateBrailleOrEnglish(input));