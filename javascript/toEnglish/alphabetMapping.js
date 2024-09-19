
const alphabet = {
  'O.....': 'a',
  'O.O...': 'b',
  'OO....': 'c',
  'OO.O..': 'd',
  'O..O..': 'e',
  'OOO...': 'f',
  'OOOO..': 'g',
  'O.OO..': 'h',
  '.OO...': 'i',
  '.OOO..': 'j',
  'O...O.': 'k',
  'O.O.O.': 'l',
  'OO..O.': 'm',
  'OO.OO.': 'n',
  'O..OO.': 'o',
  'OOO.O.': 'p',
  'OOOOO.': 'q',
  'O.OOO.': 'r',
  '.OO.O.': 's',
  '.OOOO.': 't',
  'O...OO': 'u',
  'O.O.OO': 'v',
  '.OOO.O': 'w',
  'OO..OO': 'x',
  'OO.OOO': 'y',
  'O..OOO': 'z',
}

const numbers = {
  'O.....': '1',
  'O.O...': '2',
  'OO....': '3',
  'OO.O..': '4',
  'O..O..': '5',
  'OOO...': '6',
  'OOOO..': '7',
  'O.OO..': '8',
  '.OO...': '9',
  '.OOO..': '0',
}

const symbols = {
  '..OO.O': '.',
  '..O...': ',',
  '..O.OO': '?',
  '..OOO.': '!',
  '..OO..': ':',
  '..O.O.': ';',
  '....OO': '-',
  '.O..O.': '/',
  '.OO..O': '<',
  'O..OO.': '>',
  'O.O..O': '(',
  '.O.OO.': ')',
  '......': ' ',
}

const follows = {
  '.....O': 'CAP',
  '.O...O': 'DEC',
  '.O.OOO': 'NUM',
}

module.exports = {alphabet, numbers, symbols, follows};