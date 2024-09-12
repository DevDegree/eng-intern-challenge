import { exec } from "node:child_process";
import { promisify } from "node:util";

const execAsync = promisify(exec);

describe("extra tests", () => {
	it("should translate English to Braille and back to English correctly", async () => {
		const originalText = "Hello World 123a1";

		// Translate to Braille
		const { stdout: brailleOutput } = await execAsync(
			`ts-node translator.ts ${originalText}`,
		);
		const brailleTranslation = brailleOutput.trim();

		// Translate back to English
		const { stdout: englishOutput } = await execAsync(
			`ts-node translator.ts "${brailleTranslation}"`,
		);
		const finalTranslation = englishOutput.trim();

		expect(finalTranslation).toBe(originalText);
	});
});
