const toBraille = require('../index');

describe('toBraille function', () => {
  test('returns true for a valid Braille string', () => {
    expect(toBraille('a')).toBe('O.....'); 
    expect(toBraille('dog')).toBe('OO.O..O..OO.OOOO..'); 
    expect(toBraille('world')).toBe('.OOO.OO..OO.O.OOO.O.O.O.OO.O..'); 
  });

  test('returns true for valid Braille string with capital letters', () => {
    expect(toBraille('A')).toBe('.....OO.....'); 
    expect(toBraille('Dog')).toBe('.....OOO.O..O..OO.OOOO..');
    expect(toBraille('Dog Dog')).toBe('.....OOO.O..O..OO.OOOO.............OOO.O..O..OO.OOOO..');
    expect(toBraille('World')).toBe('.....O.OOO.OO..OO.O.OOO.O.O.O.OO.O..');
  })

  test('returns true for valid braille numbers', () => {
    expect(toBraille('1')).toBe('.O.OOOO.....'); 
    expect(toBraille('123')).toBe('.O.OOOO.....O.O...OO....');
    expect(toBraille('123 ')).toBe('.O.OOOO.....O.O...OO..........');
  })

  test('translator.test.js test', () => {
    expect(toBraille('Abc 123 xYz')).toBe('.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO');
  })
});