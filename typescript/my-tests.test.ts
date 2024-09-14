import { isBraille } from "./booleans";
import englishTranslator from "./englishTranslator";

describe("test isBraille", () => {
  it("false if not a multiple of 6 characters", () => {
    let result = isBraille("O.......");
    expect(result).toBeFalsy();
  });
  it("false if it contains a letter other than O or .", () => {
    let result = isBraille("...Oa.");
    expect(result).toBeFalsy();
  });
  it("true if valid braille", () => {
    let result = isBraille("...O..");
    expect(result).toBeTruthy();
  });
  it("Hello World braille gives true", () => {
    let result = isBraille(
      ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    );
    expect(result).toBeTruthy();
  });
});

describe("Test English Translator", () => {
  it("Example 1: Hello world", () => {
    let result = englishTranslator("Hello world");
    expect(result).toBe(
      ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    );
  });

  it("Example 2: 42", () => {
    let result = englishTranslator("42");
    expect(result).toBe(".O.OOOOO.O..O.O...");
  });

  it("Example 2: 3 A2", () => {
    let result = englishTranslator("3 A2");
    expect(result).toBe(".O.OOOOO...............OO......O.OOOO.O...");
  });
});
