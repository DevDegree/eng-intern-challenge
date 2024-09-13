const BrailleEngChart = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.O.O..', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.O.OO.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
  'A': '.....OO.....', 'B': '.....OO.O...', 'C': '.....OOO....', 'D': '.....OOO.O..', 'E': '.....OO..O..', 'F': '.....OOOO...', 'G': '.....OOOOO..', 'H': '.....OO.OO..', 'I': '.....O.O.O..', 'J': '.....O.OOO..', 'K': '.....OO...O.', 'L': '.....OO.O.O.', 'M': '.....OOO..O.', 'N': '.....OOO.OO.', 'O': '.....OO..OO.', 'P': '.....OOOO.O.', 'Q': '.....OOOOOO.', 'R': '.....OO.OOO.', 'S': '.....O.O.OO.', 'T': '.....O.OOOO..', 'U': '.....OO...OO', 'V': '.....OO.O.OO', 'W': '.....O.OOO.O', 'X': '.....OOO..OO', 'Y': '.....OOO.OOO', 'Z': '.....OO..OOO',
  '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.O.O..', '0': '.OO...',
  ' ': '......'
}

const brailleToEng = (str) => {
  let isNum = false;
  let isCap = false;
  let splittedBraille = [];
  let output = '';

  for (let i = 0; i < str.length; i += 6) {
    splittedBraille.push(str.slice(i, i + 6));
  }

  for (let i = 0; i < splittedBraille.length; i++) {

    if (splittedBraille[i] === '.....O') {
      isCap = true;
      continue;
    }

    if (splittedBraille[i] === '.O.OOO') { 
      isNum = true;
      continue;
    }

   if (splittedBraille[i] === '......') {
      output += ' ';
      isNum = false;
      continue;
    }

    if (isCap) {
      output += Object.keys(BrailleEngChart).find(key => {
        return BrailleEngChart[key] === splittedBraille[i] && isNaN(key);
      }).toUpperCase();
      isCap = false;
      continue;
    }

    if (isNum) {
      output += Object.keys(BrailleEngChart).find(key => {
        return BrailleEngChart[key] === splittedBraille[i] && !isNaN(key); 
      });
      continue;
    }

    output += Object.keys(BrailleEngChart).find(key => {
      return BrailleEngChart[key] === splittedBraille[i] && isNaN(key);
    });
  }

 console.log(output);
 return;
}

const engToBraille = (str) => {
  let isNum = false;
  let output = '';
  for (let i = 0; i < str.length; i++) {
    if (str[i] === ' ') {
      output += BrailleEngChart[str[i]];
      isNum = false;
      continue;
    }

    if (!isNaN(str[i])) {
      if (!isNum) {
        output += '.O.OOO';
        isNum = true;
      }
    } else isNum = false;

    output += BrailleEngChart[str[i]];
  }

  console.log(output)
  return;
}

const isBraille = (str) => {
  if (str.includes('.')) return 1;
  else return 0;
}

const translator = () => {
  const str = process.argv.slice(2).join(' ');
  
  if (isBraille(str)) brailleToEng(str); 
  else engToBraille(str);

  return;
}

translator();