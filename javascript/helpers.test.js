const { isBraille, translateBrailleToEnglish } = require("./helpers");
const { brailleAlphabet, brailleNumber, brailleOther } = require("./constants");

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
  it("should translate a single lowercase letter", () => {
    const input = brailleAlphabet["a"]; // 'O.....'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("a");
  });

  it("should translate a single capital letter", () => {
    const input = brailleOther["CAPITAL_FOLLOWS"] + brailleAlphabet["a"]; // '.....O' + 'O.....'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("A");
  });

  it("should translate a single number", () => {
    const input = brailleOther["NUMBER_FOLLOWS"] + brailleNumber["1"]; // '.....O' + 'O.....'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("1");
  });

  it("should translate a space", () => {
    const input = brailleOther[" "]; // '......'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe(" ");
  });

  it("should translate a word with mixed case", () => {
    const input =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["h"] +
      brailleAlphabet["e"] +
      brailleAlphabet["l"] +
      brailleAlphabet["l"] +
      brailleAlphabet["o"]; // '.....O' + 'O.OO..' + 'O..O..' + 'O.O.O.' + 'O.O.O.' + 'O..OO.'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("Hello");
  });

  it("should translate a sentence with numbers and letters", () => {
    const input =
      brailleAlphabet["i"] +
      brailleAlphabet["t"] +
      brailleOther[" "] +
      brailleOther["NUMBER_FOLLOWS"] +
      brailleNumber["1"] +
      brailleNumber["2"] +
      brailleOther[" "] +
      brailleAlphabet["a"] +
      brailleAlphabet["m"]; // '.OO...' + '.OOOO.' + '......' + '.....O' + 'O.....' + 'O.O...' + '......' + 'O.....' + 'OO..O.'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("it 12 am");
  });

  it("should handle consecutive capital letters correctly", () => {
    const input =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["n"] +
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["y"]; // '.....O' + 'OO.OO.' + '.....O' + 'OO.OOO'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("NY");
  });

  it("should translate a complex sentence with spaces, numbers, and capitalization", () => {
    const input =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["h"] +
      brailleAlphabet["e"] +
      brailleAlphabet["l"] +
      brailleAlphabet["l"] +
      brailleAlphabet["o"] +
      brailleOther[" "] +
      brailleOther["NUMBER_FOLLOWS"] +
      brailleNumber["1"] +
      brailleNumber["2"] +
      brailleNumber["3"] +
      brailleOther[" "] +
      brailleAlphabet["a"] +
      brailleAlphabet["t"] +
      brailleOther[" "] +
      brailleAlphabet["x"] +
      brailleAlphabet["y"] +
      brailleAlphabet["z"]; // '.....O' + 'O.OO..' + 'O..O..' + 'O.O.O.' + 'O.O.O.' + 'O..OO.' + '......' + '.....O' + 'O.....' + 'O.O...' + 'OO....' + '......' + 'O.....' + '.OOOO.' + 'O..O..' + '......' + 'OO..OO' + 'OO.OOO' + 'O..OOO'
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("Hello 123 at xyz");
  });
});
