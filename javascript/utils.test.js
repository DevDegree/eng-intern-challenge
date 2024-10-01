const { isBraille, isCapital, isChar, isNumber, isSpace, invertObject } = require("./utils")

describe("utils", () => {
  it("should check if string is braille", () => {
    expect(isBraille("hello world")).toBe(false);
    expect(isBraille(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")).toBe(true);
  })
  it("should check if char is capitalized", () => {
    expect(isCapital("A")).toBe(true);
    expect(isCapital("b")).toBe(false);
  })
  it("should check if char is number", () => {
    expect(isNumber("1")).toBe(true);
    expect(isNumber("A")).toBe(false);
  })
  it("should check if string is char", () => {
    expect(() => isChar("hello world")).toThrow();
    expect(isChar("a")).toBe(true);
  })
  it("should check if char is space", () => {
    expect(isSpace(" ")).toBe(true);
    expect(isSpace("a")).toBe(false);
  })
  it("should invert an switch keys and values for an object", () => {
    const obj = {
      A: 1,
      B: 2,
      C: 3,
      D: 4
    }
    const expected = {
      "1": "A",
      "2": "B",
      "3": "C",
      "4": "D"
    }
    expect(invertObject(obj)).toEqual(expected)
  })
})