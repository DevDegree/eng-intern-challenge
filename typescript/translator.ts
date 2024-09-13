const args = process.argv.slice(2);
const message = args.join(' ');

const BRAILLE: {[key: string]: string} = {
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
  '.': '..OO.O',
  ' ': '......',
};

const libs = {
  capital: '.....O',
  number: '.O.OOO',
};

function translate(input: string): string {
  let output = '';
  let isNumber = false;

  for (let i = 0; i < input.length; i++) {
    const char = input[i];

    if (/[A-Z]/.test(char)) {
      output += libs.capital;
      output += BRAILLE[char.toLowerCase()];
    } else if (/[0-9]/.test(char)) {
      if (!isNumber) {
        output += libs.number;
        isNumber = true;
      }
      const letter = String.fromCharCode(char.charCodeAt(0) + 49 - 1); // Convert digit to letter
      output += BRAILLE[letter];
    } else if (char === ' ') {
      output += BRAILLE[' '];
      isNumber = false;
    } else {
      output += BRAILLE[char] || BRAILLE[' '];
    }
  }
  return output;
}

async function main() {
  const translated = translate(message || 'Hello, World!');
  console.log(translated);
}

main();
