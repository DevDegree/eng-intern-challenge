
const toEnglish = require('../index');

describe('toEnglish function', () => {
  test('tests for english to braile easy words', () => {
    expect(toEnglish('O.....')).toBe('a'); 
    expect(toEnglish('OO.O..O..OO.OOOO..')).toBe('dog'); 
    expect(toEnglish('.OOO.OO..OO.O.OOO.O.O.O.OO.O..')).toBe('world'); 
  });

  test('returns true for valid Braille string with capital letters', () => {
    expect(toEnglish('.....OO.....')).toBe('A'); 
    expect(toEnglish('.....OOO.O..O..OO.OOOO..')).toBe('Dog');
    expect(toEnglish('.....OOO.O..O..OO.OOOO.............OOO.O..O..OO.OOOO..')).toBe('Dog Dog');
    expect(toEnglish('.....O.OOO.OO..OO.O.OOO.O.O.O.OO.O..')).toBe('World');
  })

  test('returns true for valid braille numbers', () => {
    expect(toEnglish('.O.OOOO.....')).toBe('1'); 
    expect(toEnglish('.O.OOOO.....O.O...OO....')).toBe('123');
    expect(toEnglish('.O.OOOO.....O.O.....OO.OOO....')).toBe('12.3');
    expect(toEnglish('.O.OOOO.....O.O...OO..........')).toBe('123 ');
  })

  test('translator.test.js test', () => {
    expect(toEnglish('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO')).toBe('Abc 123 xYz');
  })
});