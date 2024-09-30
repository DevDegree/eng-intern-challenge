const { isBraille, isCapital, isChar, isNumber, isSpace } = require("./utils")

describe("utils", () => {
  it("checks if string is braille", () => {
    expect(isBraille("hello world")).toBe(false);
    expect(isBraille(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")).toBe(true);
  })
  it("checks if char is capitalized", () => {
    expect(isCapital("A")).toBe(true);
    expect(isCapital("b")).toBe(false);
  })
  it("checks if char is number", () => {
    expect(isNumber("1")).toBe(true);
    expect(isNumber("A")).toBe(false);
  })
  it("checks if string is char", () => {
    expect(() => isChar("hello world")).toThrow();
    expect(isChar("a")).toBe(true);
  })
  it("checks if char is space", () => {
    expect(isSpace(" ")).toBe(true);
    expect(isSpace("a")).toBe(false);
  })
})