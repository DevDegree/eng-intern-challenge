const { isBraille, translateBrailleToEnglish } = require("./helpers");
describe("isBraille", () => {
  it("should return true for a valid braille string", () => {
    expect(isBraille("O.OO.O.O")).toBe(true);
  });

  it("should return true for a valid braille string with lowercase characters", () => {
    expect(isBraille("o.oO.o.o")).toBe(true);
  });

  it("should return false for a string with invalid characters", () => {
    expect(isBraille("O.X.O")).toBe(false);
  });

  it("should return false for a string with numbers", () => {
    expect(isBraille("O.1O")).toBe(false);
  });

  it("should return false for an empty string", () => {
    expect(isBraille("")).toBe(false);
  });

  it("should return false for a string with spaces", () => {
    expect(isBraille("O.O O.O")).toBe(false);
  });

  it("should return false for a string with special characters", () => {
    expect(isBraille("O.O@O.O")).toBe(false);
  });
});

describe("translateBrailleToEnglish", () => {
  it("returns", () => {
    expect(
      translateBrailleToEnglish(
        ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
      )
    ).toBe("Abc 123 xYz");
  });
});
