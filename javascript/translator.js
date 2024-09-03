const input = '.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..';
let output;

if (input.includes('.')) {
  // Braille
  const brailleCharacters = [];
  const lengthOfInput = input.length;
  let index = 0;

  while (index <= lengthOfInput - 1) {
    const brailleCharacter = input.substring(index, index + 6);
    brailleCharacters.push(brailleCharacter);
    index += 6;
  }

  output = brailleCharacters;
} else {
  // English
  output = 'English';
}

console.log(output);