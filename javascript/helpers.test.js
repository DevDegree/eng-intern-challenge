const {
  isBraille,
  translateBrailleToEnglish,
  translateEnglishToBraille,
} = require("./helpers");
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
    const input = brailleAlphabet["a"];
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
    const input = brailleOther[" "];
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
      brailleAlphabet["o"];
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
      brailleAlphabet["m"];
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("it 12 am");
  });

  it("should handle consecutive capital letters correctly", () => {
    const input =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["n"] +
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["y"];
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
      brailleAlphabet["z"];
    const output = translateBrailleToEnglish(input);
    expect(output).toBe("Hello 123 at xyz");
  });
});

describe("translateEnglishToBraille", () => {
  it("should translate a single lowercase letter to braille", () => {
    const input = "a";
    const output = translateEnglishToBraille(input);
    expect(output).toBe(brailleAlphabet["a"]);
  });

  it("should translate a single capital letter to braille", () => {
    const input = "A";
    const output = translateEnglishToBraille(input);
    expect(output).toBe(brailleOther["CAPITAL_FOLLOWS"] + brailleAlphabet["a"]); // '.....O' + 'O.....'
  });

  it("should translate a single number to braille", () => {
    const input = "1";
    const output = translateEnglishToBraille(input);
    expect(output).toBe(brailleOther["NUMBER_FOLLOWS"] + brailleNumber["1"]); // '.....O' + 'O.....'
  });

  it("should translate a space to braille", () => {
    const input = " ";
    const output = translateEnglishToBraille(input);
    expect(output).toBe(brailleOther[" "]);
  });

  it("should translate a word with mixed case to braille", () => {
    const input = "Hello";
    const output = translateEnglishToBraille(input);
    const expectedOutput =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["h"] +
      brailleAlphabet["e"] +
      brailleAlphabet["l"] +
      brailleAlphabet["l"] +
      brailleAlphabet["o"];
    expect(output).toBe(expectedOutput);
  });

  it("should translate a sentence with numbers and letters to braille", () => {
    const input = "it 12 am";
    const output = translateEnglishToBraille(input);
    const expectedOutput =
      brailleAlphabet["i"] +
      brailleAlphabet["t"] +
      brailleOther[" "] +
      brailleOther["NUMBER_FOLLOWS"] +
      brailleNumber["1"] +
      brailleNumber["2"] +
      brailleOther[" "] +
      brailleAlphabet["a"] +
      brailleAlphabet["m"];
    expect(output).toBe(expectedOutput);
  });

  it("should handle consecutive capital letters correctly in braille", () => {
    const input = "NY";
    const output = translateEnglishToBraille(input);
    const expectedOutput =
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["n"] +
      brailleOther["CAPITAL_FOLLOWS"] +
      brailleAlphabet["y"];
    expect(output).toBe(expectedOutput);
  });

  it("should translate a complex sentence with spaces, numbers, and capitalization to braille", () => {
    const input = "Hello 123 at xyz 456";
    const output = translateEnglishToBraille(input);
    const expectedOutput =
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
      brailleAlphabet["z"] +
      brailleOther[" "] +
      brailleOther["NUMBER_FOLLOWS"] +
      brailleNumber["4"] +
      brailleNumber["5"] +
      brailleNumber["6"];
    expect(output).toBe(expectedOutput);
  });

  it("should translate multiple spaces correctly to braille", () => {
    const input = "hello  world";
    const output = translateEnglishToBraille(input);
    const expectedOutput =
      brailleAlphabet["h"] +
      brailleAlphabet["e"] +
      brailleAlphabet["l"] +
      brailleAlphabet["l"] +
      brailleAlphabet["o"] +
      brailleOther[" "] +
      brailleOther[" "] +
      brailleAlphabet["w"] +
      brailleAlphabet["o"] +
      brailleAlphabet["r"] +
      brailleAlphabet["l"] +
      brailleAlphabet["d"];
    expect(output).toBe(expectedOutput);
  });
});
