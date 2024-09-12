const englishToBraille = {
  'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
  'g': 'OOOO..', 'h': 'O.OO..', 'i': '.O.O..', 'j': '.OO...', 'k': 'O...O.', 'l': 'O.O.O.',
  'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
  's': '.O.OO.', 't': '.OO.O.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
  'y': 'OO.OOO', 'z': 'O..OOO', 'captialFollows': '.....O', 'numberFollows': '.O.OOO', ' ': '......'
};

const brailleToEnglish = {
  "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
  "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
  "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
  "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
  "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
  "O..OOO": "z", '.....O': 'captialFollows', '.O.OOO': 'numberFollows', '......': ' '

};

const brailleNumbers = {
  "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
  "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO.."
};



const translator = function(arg) {

  const brailleEnglish = arg.match(/^[O.]+$/); //checking if the user input is english or braille
  let result = "";
  let number = false;
  let capital = false;

  if (!brailleEnglish) {
    //loop through the input string and change every character to braille
    for (let character of arg) {
      if (character === " ") {
        result += englishToBraille[" "];
        number = false;
      } else if (character.match(/[A-Z]/)) {
        result += englishToBraille["captialFollows"];
        result += englishToBraille[character.toLowerCase()];
        number = false;
      } else if (character.match(/[a-z]/)) {
        result += englishToBraille[character];
        number = false;
      } else if (character >= 0 && character <= 9) {
        if (!number) {
          result += englishToBraille["numberFollows"];
          number = true;
        }
        result += brailleNumbers[character];
      
      }
    
    }
  } else {
    
    let brailleSet = arg.match(/.{1,6}/g); //getting brailler characters which is every 6 characters
    //loop through the braille characters and change them to english
    for (let character of brailleSet) {
      if (character === englishToBraille[" "]) {
        result += " ";
        number = false;
      } else if (character === englishToBraille["captialFollows"]) {
        capital = true;
      } else if (character === englishToBraille["numberFollows"]) {
        number = true;
      } else if (number) {
        for (let key in brailleNumbers) {
          if (brailleNumbers[key] === character) {
            result += key;
          }
        }
      } else if (capital) {
        result += character.toUpperCase();
        capital = false;
      } else {
        result += brailleToEnglish[character];
      }
    }
  }
  return result;
};


const input = process.argv.slice(2).join(' '); //gets user input
if (input) {
  console.log(translator(input));
}