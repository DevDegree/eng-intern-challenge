const brailleAlphabet = {
  a: 'O.....',
  b: 'O.O...',
  c: 'OO....',
  d: 'OO.O..',
  e: 'O..O..',
  f: 'OOO...',
  g: 'OOOO..',
  h: 'O.OO..',
  i: '.OO...',
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
  
  //Numbers(0-9)
  '1': 'O.....',
  '2': 'O.O...',
  '3': 'OO....',
  '4': 'OO.O..',
  '5': 'O..O..',
  '6': 'OOO...',
  '7': 'OOOO..',
  '8': 'O.OO..',
  '9': '.OO...',
  '0': '.OOO..',
  
  // Special symbols
  ' ': '......', //space
  capital: '.....O',
  number: 'O.OOOO',

	// Punctuation
	'.': '..OO.O',
	',': '..O...',
	'?': '..O.OO',
	'!': '..OOO.',
	':': '..OO..',
	';': '..O.O.',
	'-': '....OO',
	'/': '.O..O.',
	'<': '.OO..O',
	'>': 'O..OO.',
	'(': 'O.O..O',
	')': '.O.OO.'
};

// 1. Check if its braille (contain only 'O' and '.') OR letters/num/punc
// 2.
// 3.
// 4.
// 5.

	//check if Braille contains only 'O' and '.'
function isBraille(input) {
	for (let i = 0; i < input.length; i++) {
		const char = input[i];
		if (char !=='O' && char !== '.') {
			return false;
		}
	}

	//check if its divisible by 6
	if (input.length % 6 !== 0) {
		return false;
	}
	return true;
}

const input1 = 'O.....O.OO...O...O....'; 
const input2 = 'O..O..O.OO..'; 
const input3 = 'O...X...'; 

console.log(isBraille(input1));
console.log(isBraille(input2)); 
console.log(isBraille(input3));