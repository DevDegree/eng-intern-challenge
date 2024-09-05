import { argv } from 'process';

// I was able to get the alphabet to translate to braille, but not the other way around and not including numbers or capitals. I hope this is enough to show that I understand the concept of the challenge. I'm sorry I couldn't figure out the rest. I hope you have a great day!

const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", " "];
const brailleAlphabet = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.OOOO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "..OO.O", "......"];

const input = argv.slice(2);

const translate = (input) => {
  const lowercase= input.toString().toLowerCase();
  const splitInput = lowercase.split('');
      const alphabetIndex = splitInput.map(letter => alphabet.indexOf(letter) + 1);
      const translated = alphabetIndex.map(index => brailleAlphabet[index]);
  return translated.toString().replaceAll(',', '');
};

console.log(translate(input));