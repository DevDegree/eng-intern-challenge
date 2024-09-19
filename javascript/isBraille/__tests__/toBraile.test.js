const isBraille = require('../index');

describe('isBraille function', () => {
  test('returns true for a valid Braille string', () => {
    expect(isBraille('O.O.OO')).toBe(true);
    expect(isBraille('O.O.OO.O.O.O')).toBe(true);
    expect(isBraille('O.OO..')).toBe(true);
  })

  test('returns false for a string not divisible by 6', () => {
    expect(isBraille('O.O')).toBe(false);
    expect(isBraille('O.O.O')).toBe(false);
    expect(isBraille('O.O.OOO')).toBe(false);
  })

  test('returns false for a string containing invalid characters', () => {
    expect(isBraille('O.O.XO')).toBe(false);
    expect(isBraille('O.OO,')).toBe(false);
    expect(isBraille('')).toBe(false);
  })

  test('returns false for an empty string', () => {
    expect(isBraille('')).toBe(false);
  })

  test('returns false for strings with characters other than "." and "O"', () => {
    expect(isBraille('O.OO!O')).toBe(false);
    expect(isBraille('OO.O0.')).toBe(false);
    expect(isBraille('O..O$O')).toBe(false);
  })

  test('handles edge cases correctly', () => {
    expect(isBraille('.O.O.O')).toBe(true);
    expect(isBraille('OO....')).toBe(true);
  })
})