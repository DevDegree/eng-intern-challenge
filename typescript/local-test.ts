// Note: This file must be change to a .test.ts file in order to work

import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

describe("translator.ts output", () => {
  it("should print the correct output to the console", async () => {
    const { stdout } = await execAsync("ts-node translator.ts Abc 123 xYz");

    const expected =
      ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO";
    expect(stdout.trim()).toBe(expected);
  });

  it("should translate Braille to English", async () => {
    const { stdout } = await execAsync(
      "ts-node translator.ts O..........OO.....O......O.OOOO....."
    );

    expect(stdout.trim()).toBe("aAa1");
  });

  it("should translate English with upper and lowercase letters and spaces", async () => {
    const { stdout } = await execAsync("ts-node translator.ts Hello world");
    const expected =
      ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";

    expect(stdout.trim()).toBe(expected);
  });

  it("should translate numbers into Braille", async () => {
    const { stdout } = await execAsync("ts-node translator.ts 42");
    const expected = ".O.OOOOO.O..O.O...";

    expect(stdout.trim()).toBe(expected);
  });
});

describe("translator.ts error handling", () => {
  it("should print an error log when no argument is provided", async () => {
    const { stdout } = await execAsync("ts-node translator.ts");

    expect(stdout.trim()).toMatch(/no input detected/i);
  });

  it("should print an error log if a mix of english and braille is provided", async () => {
    const { stdout } = await execAsync(
      "ts-node translator.ts O..OOOO..OO.O..OO.zzzoooo"
    );

    expect(stdout.trim()).toMatch(/invalid input/i);
  });

  it("should print an error log if an un-supported English character is detected", async () => {
    const { stdout } = await execAsync("ts-node translator.ts Hello world!");

    expect(stdout.trim()).toMatch(/invalid input/i);
  });

  it("should print an error log if an unsupported or invalid braille character is provided", async () => {
    const { stdout } = await execAsync(
      "ts-node translator.ts ..O.OO..OOO.O.O..O.O.OO."
    );

    expect(stdout.trim()).toMatch(/invalid braille/i);
  });

  it("should print an error if consecutive capital prefixes are provided", async () => {
    const { stdout } = await execAsync(
      "ts-node translator.ts .O.OOO.O.OOOOO.O.."
    );

    expect(stdout.trim()).toMatch(/invalid braille/i);
  });

  it("should print an error log if consecutive number prefixes are provided", async () => {
    const { stdout } = await execAsync(
      "ts-node translator.ts .....OOOO.O......O.....O"
    );

    expect(stdout.trim()).toMatch(/invalid braille/i);
  });
});
