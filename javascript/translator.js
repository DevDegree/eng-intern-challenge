const input = '.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO';
let output;

if (input.includes('.')) {
  // Input in braille
  const brailleCharacters = [];
  const lengthOfInput = input.length;
  let index = 0;

  while (index <= lengthOfInput - 1) {
    const brailleCharacter = input.substring(index, index + 6);
    brailleCharacters.push(brailleCharacter);
    index += 6;
  }

  const englishCharacters = [];
  let isCapital = false;
  let isNumber = false;

  for (const brailleCharacter of brailleCharacters) {
    let englishCharacter = '';
    
    switch (brailleCharacter) {
      case '.....O':
        isCapital = true;
        break;
      case '.O.OOO':
        isNumber = true;
        break;
      case '......':
        englishCharacter = ' ';
        isNumber = false;
        break;
      case 'O.....':
        if (isNumber) {
          englishCharacter = '1';
        } else {
          englishCharacter = 'a';
        }
        break;
      case 'O.O...':
        if (isNumber) {
          englishCharacter = '2';
        } else {
          englishCharacter = 'b';
        }
        break;
      case 'OO....':
        if (isNumber) {
          englishCharacter = '3';
        } else {
          englishCharacter = 'c';
        }
        break;
      case 'OO.O..':
        if (isNumber) {
          englishCharacter = '4';
        } else {
          englishCharacter = 'd';
        }
        break;
      case 'O..O..':
        if (isNumber) {
          englishCharacter = '5';
        } else {
          englishCharacter = 'e';
        }
        break;
      case 'OOO...':
        if (isNumber) {
          englishCharacter = '6';
        } else {
          englishCharacter = 'f';
        }
        break;
      case 'OOOO..':
        if (isNumber) {
          englishCharacter = '7';
        } else {
          englishCharacter = 'g';
        }
        break;
      case 'O.OO..':
        if (isNumber) {
          englishCharacter = '8';
        } else {
          englishCharacter = 'h';
        }
        break;
      case '.OO...':
        if (isNumber) {
          englishCharacter = '9';
        } else {
          englishCharacter = 'i';
        }
        break;
      case '.OOO..':
        if (isNumber) {
          englishCharacter = '0';
        } else {
          englishCharacter = 'j';
        }
        break;
      case 'O...O.':
        englishCharacter = 'k';
        break;
      case 'O.O.O.':
        englishCharacter = 'l';
        break;
      case 'OO..O.':
        englishCharacter = 'm';
        break;
      case 'OO.OO.':
        englishCharacter = 'n';
        break;
      case 'O..OO.':
        englishCharacter = 'o';
        break;
      case 'OOO.O.':
        englishCharacter = 'p';
        break;
      case 'OOOOO.':
        englishCharacter = 'q';
        break;
      case 'O.OOO.':
        englishCharacter = 'r';
        break;
      case '.OO.O.':
        englishCharacter = 's';
        break;
      case '.OOOO.':
        englishCharacter = 't';
        break;
      case 'O...OO':
        englishCharacter = 'u';
        break;
      case 'O.O.OO':
        englishCharacter = 'v';
        break;
      case '.OOO.O':
        englishCharacter = 'w';
        break;
      case 'OO..OO':
        englishCharacter = 'x';
        break;
      case 'OO.OOO':
        englishCharacter = 'y';
        break;
      case 'O..OOO':
        englishCharacter = 'z';
        break;
    }
    
    if (englishCharacter) {
      if (isCapital) {
        englishCharacter = englishCharacter.toUpperCase();
        isCapital = false;
      }
      
      englishCharacters.push(englishCharacter);
    }
  }

  output = englishCharacters.join('');
} else {
  // Input in English
  output = 'English';
}

console.log(output);