
const alphabet = {
  'A': "O.....",
  'B': "O.O...",
  'C': "OO....",
  'D': "OO.O..",
  'E': "O..O..",
  'F': "OOO...",
  'G': "OOOO..",
  'H': "O.OO..",
  'I': ".OO...",
  'J': ".OOO..",
  'K': "O...O.",
  'L': "O.O.O.",
  'M': "OO..O.",
  'N': "OO.OO.",
  'O': "O..OO.",
  'P': "OOO.O.",
  'Q': "OOOOO.",
  'R': "O.OOO.",
  'S': ".OO..O",
  'T': ".OOO.O",
  'U': "O...OO",
  'V': "O.O.OO",
  'W': ".OOO.O",
  'X': "OO..OO",
  'Y': "OO.OOO",
  'Z': "O..OOO",
}

const numbers = Object.values(alphabet).slice(0, 9);
numbers.unshift(alphabet["J"]) // 0 value is the same as J
const markers = {
  capital: ".....O",
  number: ".O.OOO"
}

module.exports = {
  alphabet,
  numbers,
  markers
}