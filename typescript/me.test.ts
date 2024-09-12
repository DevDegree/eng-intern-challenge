import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

const execTranslator = async (input: string, expected: string) => {
  const { stdout, stderr } = await execAsync(`ts-node translator.ts ${input}`);
  expect(stderr).toBe("");
  expect(stdout.trim()).toBe(expected);
};

const expectDoubleConversionToWork = async (input: string) => {
  const { stdout, stderr } = await execAsync(`ts-node translator.ts ${input}`);
  expect(stderr).toBe("");

  await execTranslator(stdout.trim(), input);
};

describe("my translator.js test scripts", () => {
  it("hello world", async () => {
    await execTranslator(
      "Hello world",
      ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
    );
  });

  it("42", async () => {
    await execTranslator("42", ".O.OOOOO.O..O.O...");
  });

  it(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....", async () => {
    await execTranslator(
      ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....",
      "Abc 123"
    );
  });

  it("Braille to English to Braille", async () => {
    const input = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....";
    await expectDoubleConversionToWork(input);
  });

  it("should handle text that has only 'O'", async () => {
    const input = "OO";
    const expected = ".....OO..OO......OO..OO.";

    await execTranslator(input, expected);
  });

  it("random", async () => {
    const ranges = [
      [48, 57],
      [65, 90],
      [97, 122],
    ];

    let input = "";

    for (let i = 0; i < 100; i++) {
      const range = ranges[Math.floor(Math.random() * ranges.length)];

      let text = "";

      for (let j = 0; j < 10; j++) {
        text += String.fromCharCode(
          Math.floor(Math.random() * (range[1] - range[0]) + range[0])
        );
      }

      input += text + " ";
    }

    input = input.trim();

    await expectDoubleConversionToWork(input);
  });

  it("should handle expected input", async () => {
    await execTranslator("", "");
  });

  it("should handle only spaces", async () => {
    await execTranslator(" ", "");
  });

  it("random2", async () => {
    const alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let text = "";
    for (let i = 0; i < 100; i++) {
      text += alphabet[Math.floor(Math.random() * alphabet.length)];
    }
    await expectDoubleConversionToWork(text);
  });
});
