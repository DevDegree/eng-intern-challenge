import { exec } from "node:child_process";
import { promisify } from "node:util";

const execAsync = promisify(exec);

describe("extra tests", () => {
	const runTranslation = async (input: string) => {
		const { stdout, stderr } = await execAsync(
			`ts-node translator.ts ${input}`,
		);
		return stderr.length > 0 ? stderr.trim() : stdout.trim();
	};

	const runBidirectionalTranslation = async (
		englishInput: string,
		brailleInput: string,
	) => {
		const brailleOutput = await runTranslation(englishInput);
		const englishOutput = await runTranslation(brailleInput);
		expect(brailleOutput).toBe(brailleInput);
		expect(englishOutput).toBe(englishInput);
	};

	it("should translate English to Braille and back to English correctly", async () => {
		const englishInput = "Hello World 123";
		const brailleOutput = await runTranslation(englishInput);
		const englishOutput = await runTranslation(brailleOutput);
		expect(englishOutput).toBe(englishInput);
	});

	it("should handle empty input", async () => {
		const input = "";
		const result = await runTranslation(input);
		expect(result).toBe("");
	});

	it("should handle all uppercase text", async () => {
		const englishInput = "ALL CAPS";
		const brailleInput =
			".....OO..........OO.O.O......OO.O.O............OOO.........OO..........OOOO.O......O.OO.O.";
		await runBidirectionalTranslation(englishInput, brailleInput);
	});

	it("should handle mixed case text", async () => {
		const englishInput = "MiXeD cAsE";
		const brailleInput =
			".....OOO..O..OO........OOO..OOO..O.......OOO.O........OO.........OO......OO.O......OO..O..";
		await runBidirectionalTranslation(englishInput, brailleInput);
	});

	it("should handle words ending with numbers", async () => {
		const englishInput = "abc123 def456";
		const brailleInput =
			"O.....O.O...OO.....O.OOOO.....O.O...OO..........OO.O..O..O..OOO....O.OOOOO.O..O..O..OOO...";
		await runBidirectionalTranslation(englishInput, brailleInput);
	});

	it("should handle input with only numbers", async () => {
		const englishInput = "123 456 789";
		const brailleInput =
			".O.OOOO.....O.O...OO...........O.OOOOO.O..O..O..OOO..........O.OOOOOOO..O.OO...OO...";
		await runBidirectionalTranslation(englishInput, brailleInput);
	});

	it("should handle single letter words", async () => {
		const englishInput = "a b c D E f";
		const brailleInput =
			"O...........O.O.........OO...............OOO.O.............OO..O........OOO...";
		await runBidirectionalTranslation(englishInput, brailleInput);
	});

	it("should handle multiple spaces", async () => {
		const englishInput = "Hello   World"; // Three spaces between words
		const brailleOutput = await runTranslation(englishInput);
		const result = await runTranslation(brailleOutput);
		expect(result).toBe("Hello World"); // Should collapse to single space
	});

	it("should throw an error for Braille input with invalid length", async () => {
		expect(await runTranslation(".O.O")).toBe(
			"Translation error: Invalid Braille input length.",
		);
	});

	it("should throw an error for unsupported characters in English input", async () => {
		expect(await runTranslation("Hello @World")).toBe(
			"Translation error: Unsupported character: '@'",
		);
	});
});
