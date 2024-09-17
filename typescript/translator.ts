import { BidirectionalMap } from './bidirectional-map';

const input: string = process.argv.splice(2).join(' ');

enum Encoder {
  Capital = 1,
  Decimal = 2,
  Number = 3
}

const brailleAlphabetMapping = new BidirectionalMap<string, string>([
  [ 'a', 'O.....' ],
  [ 'b', 'O.O...' ],
  [ 'c', 'OO....' ],
  [ 'd', 'OO.O..' ],
  [ 'e', 'O..O..' ],
  [ 'f', 'OOO...' ],
  [ 'g', 'OOOO..' ],
  [ 'h', 'O.OO..' ],
  [ 'i', '.OO...' ],
  [ 'j', '.OOO..' ],
  [ 'k', 'O...O.' ],
  [ 'l', 'O.O.O.' ],
  [ 'm', 'OO..O.' ],
  [ 'n', 'OO.OO.' ],
  [ 'o', 'O..OO.' ],
  [ 'p', 'OOO.O.' ],
  [ 'q', 'OOOOO.' ],
  [ 'r', 'O.OOO.' ],
  [ 's', '.OO.O.' ],
  [ 't', '.OOOO.' ],
  [ 'u', 'O...OO' ],
  [ 'v', 'O.O.OO' ],
  [ 'w', '.OOO.O' ],
  [ 'x', 'OO..OO' ],
  [ 'y', 'OO.OOO' ],
  [ 'z', 'O..OOO' ]
]);

const brailleNumberMapping = new BidirectionalMap<string, string>([
  [ '0', '.OOO..' ],
  [ '1', 'O.....' ],
  [ '2', 'O.O...' ],
  [ '3', 'OO....' ],
  [ '4', 'OO.O..' ],
  [ '5', 'O..O..' ],
  [ '6', 'OOO...' ],
  [ '7', 'OOOO..' ],
  [ '8', 'O.OO..' ],
  [ '9', '.OO...' ]
]);

const brailleEncoderMapping = new BidirectionalMap<Encoder, string>([
  [ Encoder.Capital, '.....O' ],
  [ Encoder.Decimal, '.O...O' ],
  [ Encoder.Number,  '.O.OOO' ]
]);

const brailleSymbolMapping = new BidirectionalMap<string, string>([
  [ '.', '..OO.O' ],
  [ ',', '..O...' ],
  [ '?', '...OOO' ],
  [ '!', '..OOO.' ],
  [ '_', '....OO' ],
  [ '/', '.O..O.' ],
  [ '<', '.OO..O' ],
  [ '>', 'O..OO.' ],
  [ '(', 'O.O..O' ],
  [ ')', '.O.OO.' ],
  [ ' ', '......' ]
]);

/** @returns Returns true if `str` is braille, false otherwise. */
function isBraille(str: string): boolean {
  // checks if str.length is a multiple of 6 and only including 'O' and '.'
  return str.length % 6 === 0 && /^[O|\.]+$/.test(str);
}

function englishToBraille(str: string): string {
  let out: string = '';
  let onNumber: boolean = false;
  console.error(str);
  for (let char of str) {
    if (/[A-Z|a-z]/.test(char)) {
      if (/[A-Z]/.test(char)) {
        // capital prefix
        out += brailleEncoderMapping.getValue(Encoder.Capital);
        onNumber = false;
      }
      out += brailleAlphabetMapping.getValue(char.toLowerCase());
    } else if (/[0-9]/.test(char)) {
      if (!onNumber) {
        // number prefix
        out += brailleEncoderMapping.getValue(Encoder.Number);
        onNumber = true;
      }
      out += brailleNumberMapping.getValue(char);
    } else {
      const symbol = brailleSymbolMapping.getValue(char);
      onNumber = false;
      out += brailleSymbolMapping.getValue(char);
    }
  }
  return out;
}

function brailleToEnglish(str: string) {
  let out: string = '';
  let nextCapital: boolean = false;
  let onNumber: boolean = false;
  for (let i = 0; i < str.length; i += 6) {
    const braille = str.slice(i, i + 6);
    if (brailleAlphabetMapping.hasValue(braille) && !onNumber) {
      const letter = brailleAlphabetMapping.getKey(braille);
      if (nextCapital) {
        nextCapital = false;
        out += letter?.toUpperCase();
      } else {
        out += letter;
      }
    } else if (brailleSymbolMapping.hasValue(braille)) {
      const symbol = brailleSymbolMapping.getKey(braille);
      out += symbol;
      if (symbol === ' ') {
        onNumber = false;
      }
    } else if (onNumber) {
      if (brailleNumberMapping.hasValue(braille)) {
        out += brailleNumberMapping.getKey(braille);
      } else {
        return console.error('Invalid braille number after \'number follows\' symbol.');
      }
    } else if (brailleEncoderMapping.hasValue(braille)) {
      switch (brailleEncoderMapping.getKey(braille)) {
        case Encoder.Capital:
          nextCapital = true;
          break;
        case Encoder.Number:
          onNumber = true;
          break;
      }
    }
  }
  return out;
}

function translate(str: string) {
  if (isBraille(str)) {
    return brailleToEnglish(str);
  } else {
    return englishToBraille(str);
  }
}

console.log(translate(input));