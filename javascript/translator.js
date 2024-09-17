const alphabet = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO", ' ': "......"
  };
  
  const numbers = {
    '0': "OOOOO.", '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO..."
  };
  
  function convertEngToBraille(input) {
    return input.toLowerCase().split('').map(char => {
      if (char >= 'a' && char <= 'z') return alphabet[char];
      if (char >= '0' && char <= '9') return ".O.OOO" + numbers[char];
      if (char === ' ') return alphabet[' '];
      return '';
    }).join('');
  }
  
  function convertBrailleToEng(input) {
    const brailleCells = input.match(/.{6}/g) || [];
    return brailleCells.map(cell => {
      if (cell === ".O.OOO") return Object.keys(numbers).find(key => numbers[key] === cell);
      return Object.keys(alphabet).find(key => alphabet[key] === cell);
    }).join('');
  }
  
  // Determine if input is Braille or English
  const input = process.argv[2];
  
  if (/^[O.]+$/.test(input)) { // Braille contains only 'O' and '.'
    console.log(convertBrailleToEng(input));
  } else {
    console.log(convertEngToBraille(input));
  }
  