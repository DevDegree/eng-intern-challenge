const args = process.argv.slice(2);
const input = args.join(' ');

const brailleCharacters = [];
let englishCharacters = [];
let isCapital = false;
let isNumber = false;
let output;

if (input.includes('.')) {
  // Input in braille
  const lengthOfInput = input.length;
  let index = 0;

  while (index <= lengthOfInput - 1) {
    const brailleCharacter = input.substring(index, index + 6);
    brailleCharacters.push(brailleCharacter);
    index += 6;
  }

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
  englishCharacters = input.split('');

  for (const englishCharacter of englishCharacters) {
    const englishCharacterInLowerCase = englishCharacter.toLowerCase();
    let modifier = '';
    let brailleCell = '';

    if (englishCharacter === ' ') {
      modifier = '......';
      isNumber = false;
    } else if (!isNaN(englishCharacter)) {
      if (!isNumber) {
        isNumber = true;
        modifier = '.O.OOO';
      }
    } else if (englishCharacter === englishCharacter.toUpperCase()) {
      modifier = '.....O';
    }

    switch (englishCharacterInLowerCase) {
      case '1':
      case 'a':
        brailleCell = 'O.....';
        break;
      case '2':
      case 'b':
        brailleCell = 'O.O...';
        break;
      case '3':
      case 'c':
        brailleCell = 'OO....';
        break;
      case '4':
      case 'd':
        brailleCell = 'OO.O..';
        break;
      case '5':
      case 'e':
        brailleCell = 'O..O..';
        break;
      case '6':
      case 'f':
        brailleCell = 'OOO...';
        break;
      case '7':
      case 'g':
        brailleCell = 'OOOO..';
        break;
      case '8':
      case 'h':
        brailleCell = 'O.OO..';
        break;
      case '9':
      case 'i':
        brailleCell = '.OO...';
        break;
      case '0':
      case 'j':
        brailleCell = '.OOO..';
        break;
      case 'k':
        brailleCell = 'O...O.';
        break;
      case 'l':
        brailleCell = 'O.O.O.';
        break;
      case 'm':
        brailleCell = 'OO..O.';
        break;
      case 'n':
        brailleCell = 'OO.OO.';
        break;
      case 'o':
        brailleCell = 'O..OO.';
        break;
      case 'p':
        brailleCell = 'OOO.O.';
        break;
      case 'q':
        brailleCell = 'OOOOO.';
        break;
      case 'r':
        brailleCell = 'O.OOO.';
        break;
      case 's':
        brailleCell = '.OO.O.';
        break;
      case 't':
        brailleCell = '.OOOO.';
        break;
      case 'u':
        brailleCell = 'O...OO';
        break;
      case 'v':
        brailleCell = 'O.O.OO';
        break;
      case 'w':
        brailleCell = '.OOO.O';
        break;
      case 'x':
        brailleCell = 'OO..OO';
        break;
      case 'y':
        brailleCell = 'OO.OOO';
        break;
      case 'z':
        brailleCell = 'O..OOO';
        break;
    }

    brailleCharacters.push(modifier + brailleCell);
  }

  output = brailleCharacters.join('');
}

console.log(output);