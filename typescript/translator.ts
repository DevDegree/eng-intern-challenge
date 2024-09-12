import { ENGLISH_TO_BRAILLE_MAP, BRAILLE_TO_ENGLISH_MAP } from "./constants";

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
	const { characters, digits, special } = BRAILLE_TO_ENGLISH_MAP;
	let translation = "";
	let capitalNext = false;
	let numberMode = false;

	for (const segment of segments) {
		if (segment === special.capitalFollows) {
			capitalNext = true;
			continue;
		}
		if (segment === special.numberFollows) {
			numberMode = true;
			continue;
		}

		if (capitalNext) {
			// Capitalize the character and add it to the translation
			translation += characters[segment].toUpperCase();
			capitalNext = false;
		} else if (numberMode) {
			// Handle numbers
			if (segment === special.space) {
				// End of number sequence
				translation += " ";
				numberMode = false;
			} else {
				translation += digits[segment];
			}
		} else {
			// Handle alphabetic characters
			translation += characters[segment];
		}
	}
	return translation;
}

/**
 * Translates English input to Braille.
 * @param input - An array of English words.
 * @returns The translated Braille string.
 */
function translateEnglish(input: string[]): string {
	const { characters, digits, special } = ENGLISH_TO_BRAILLE_MAP;
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
					translation += special.numberFollows;
				}
				translation += digits[char];
			} else {
				// Handle alphabetic characters
				if (numberMode) {
					// Exit number mode since we encountered an alphabetic character
					numberMode = false;
					if (j !== word.length - 1) {
						// Add a space to indicate the end of a number sequence, unless it's the last number in the word
						translation += special.space;
					}
				}
				if (char.match(/[A-Z]/)) {
					// Handle uppercase characters
					translation +=
						special.capitalFollows + characters[char.toLowerCase()];
				} else {
					// Handle lowercase characters
					translation += characters[char];
				}
			}
		}
		// Add space indicator between words, except for the last word
		if (i !== input.length - 1) {
			translation += special.space;
		}
		numberMode = false; // Reset number mode after each word (because space is the indicator for the end of a number sequence)
	}

	return translation;
}

/**
 * Main function to handle input, translation, and output.
 */
function main() {
	try {
		const input: string[] = process.argv.slice(2);
		const isBraille = isInputBraille(input);
		const translation: string = isBraille
			? translateBraille(input[0])
			: translateEnglish(input);
		console.log(translation);
	} catch (error) {
		if (error instanceof Error) {
			console.error("Translation error: ", error.message);
		} else {
			console.error("An unknown error occurred", error);
		}
	}
}

main();
