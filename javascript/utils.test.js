const { isBraille, isCapital, isChar, isNumber, isSpace } = require("./utils")

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
})