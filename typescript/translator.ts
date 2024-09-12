import {
	ENGLISH_TO_BRAILLE_MAP,
	BRAILLE_TO_ENGLISH_MAP,
	SPECIAL_BRAILLE_INDICATORS,
} from "./constants";

/**
 * Determines if the input is in Braille format.
 * @param input - An array of strings to check.
 * @returns True if the input is in Braille format, false otherwise.
 */
function isInputBraille(input: string[]): boolean {
	if (input.length > 1) return false; // Braille input should be a single element (no spaces)
	const brailleRegex = new RegExp(/^[.O]+$/); // Braille input should only include '.' and 'O'
	return brailleRegex.test(input[0]);
}

/**
 * Translates Braille input to English.
 * @param input - A string of Braille characters.
 * @returns The translated English string.
 */
function translateBraille(input: string): string {
	const segments = input.match(/.{1,6}/g) || []; // Convert the input string to an array of 6-character segments
	const { characters, digits } = BRAILLE_TO_ENGLISH_MAP;
	let translation = "";
	let capitalNext = false;
	let numberMode = false;

	for (const segment of segments) {
		// Handle capital indicator - this is the indicator for the start of a word
		if (segment === SPECIAL_BRAILLE_INDICATORS.capitalFollows) {
			capitalNext = true;
			continue;
		}
		// Handle number mode - this is the indicator for the start of a number sequence
		if (segment === SPECIAL_BRAILLE_INDICATORS.numberFollows) {
			numberMode = true;
			continue;
		}
		// Handle space indicator - this is the indicator for the end of a word
		if (segment === SPECIAL_BRAILLE_INDICATORS.space) {
			if (!numberMode) {
				translation += " ";
			}
			numberMode = false;
			continue;
		}

		let char = "";
		if (numberMode) {
			char = digits[segment] || "";
			if (char === "") numberMode = false; // Exit number mode if not a valid digit
		}
		if (char === "") {
			// Not a number, or exited number mode
			char = characters[segment] || "";
		}

		if (capitalNext) {
			char = char.toUpperCase();
			capitalNext = false;
		}

		translation += char;
	}
	return translation;
}

/**
 * Translates English input to Braille.
 * @param input - An array of English words.
 * @returns The translated Braille string.
 */
function translateEnglish(input: string[]): string {
	const { characters, digits } = ENGLISH_TO_BRAILLE_MAP;
	let translation = "";
	let numberMode = false;

	for (let i = 0; i < input.length; i++) {
		const word = input[i];
		for (let j = 0; j < word.length; j++) {
			const char = word[j];

			if (char.match(/[0-9]/)) {
				// Handle numbers
				if (!numberMode) {
					// Add number indicator if not already in number mode
					numberMode = true;
					translation += SPECIAL_BRAILLE_INDICATORS.numberFollows;
				}
				translation += digits[char];
				continue;
			}

			// Handle alphabetic characters

			if (numberMode) {
				// Exit number mode since we encountered an alphabetic character
				numberMode = false;
				// Add a space to indicate the end of a number sequence, unless it's the last number in the word
				translation += SPECIAL_BRAILLE_INDICATORS.space;
			}

			if (char.match(/[A-Z]/)) {
				// Handle uppercase characters
				translation +=
					SPECIAL_BRAILLE_INDICATORS.capitalFollows +
					characters[char.toLowerCase()];
			} else {
				// Handle lowercase characters
				translation += characters[char];
			}
		}
		// Add space indicator between words, except for the last word
		if (i !== input.length - 1) {
			translation += SPECIAL_BRAILLE_INDICATORS.space;
		}
		numberMode = false; // Reset number mode after each word (because space is the indicator for the end of a number sequence)
	}

	return translation;
}

/**
 * Main function to handle input, translation, and output.
 */
function main(): string | undefined {
	try {
		const input: string[] = process.argv.slice(2);
		const isBraille = isInputBraille(input);
		const translation: string = isBraille
			? translateBraille(input[0])
			: translateEnglish(input);
		console.log(translation);
		return translation;
	} catch (error) {
		if (error instanceof Error) {
			console.error("Translation error: ", error.message);
		} else {
			console.error("An unknown error occurred", error);
		}
	}
}

main();
