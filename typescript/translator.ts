// Map from letters to their braille representation
const brailleLetterAlphabet: Record<string, string> = {
	a: 'O.....', b: 'O.O...', c: 'OO....', d: 'OO.O..',
	e: 'O..O..', f: 'OOO...', g: 'OOOO..', h: 'O.OO..',
	i: '.OO...', j: '.OOO..', k: 'O...O.', l: 'O.O.O.',
	m: 'OO..O.', n: 'OO.OO.', o: 'O..OO.', p: 'OOO.O.',
	q: 'OOOOO.', r: 'O.OOO.', s: '.OO.O.', t: '.OOOO.',
	u: 'O...OO', v: 'O.O.OO', w: '.OOO.O', x: 'OO..OO',
	y: 'OO.OOO', z: 'O..OOO'
};

// Map from numbers to the letter they share a braille representation with
const numberModeMappings: Record<string, string> = {
	'1': 'a', '2': 'b', '3': 'c', '4': 'd',
	'5': 'e', '6': 'f', '7': 'g', '8': 'h',
	'9': 'i', '0': 'j',
};

// Special braille sequences that change operating modes
enum ControlSequences {
	CAPITAL = '.....O',
	NUMBER = '.O.OOO',
	SPACE = '......'
};

const englishLettersToBraille = {
	...brailleLetterAlphabet,
	// Map uppercase letters to "capital follows" plus the letter's braille representation
	...Object.fromEntries(
		Object.entries(brailleLetterAlphabet)
			.map(([letter, braille]) => [
				letter.toUpperCase(),
				ControlSequences.CAPITAL + braille
			])
	)
};

const englishNumbersToBraille = Object.fromEntries(
	Object.entries(numberModeMappings)
		.map(([number, letter]) => [
			number,
			// Get the braille representation for the equivalent letter
			brailleLetterAlphabet[letter]
		])
);

const brailleLettersToEnglish = Object.fromEntries(
	Object.entries(brailleLetterAlphabet)
		.map(([letter, braille]) => [braille, letter])
);

const brailleNumbersToEnglish = Object.fromEntries(
	Object.entries(numberModeMappings)
		.map(([number, letter]) => [
			// Get the braille representation for the equivalent letter
			brailleLetterAlphabet[letter],
			number
		])
);

// Error with translation between English and Braille
class TranslatorError extends Error {}

// Check if the given string is in Braille
function isBraille(input: string) {
	// Braille is defined is groups of 6 characters
	return input.length % 6 === 0 && /^[.O]/.test(input);
}

// Translate a Braille string to English
function translateToEnglish(brailleStr: string) {
	// Split the Braille string into groups of 6 for each Braille sequence
	const brailleSequences = brailleStr.match(/.{6}/g)!;

	let output = '';
	let capitalMode = false;
	let numberMode = false;

	for (const seq of brailleSequences) {
		if (seq === ControlSequences.CAPITAL) {
			// Handled below
		} else if (seq === ControlSequences.NUMBER) {
			numberMode = true;
		} else if (seq === ControlSequences.SPACE) {
			numberMode = false; // Spaces end number mode
			output += ' ';
		} else if (numberMode) {
			if (!(seq in brailleNumbersToEnglish))
				throw new TranslatorError(`Unsupported sequence in number mode "${seq}"`);

			output += brailleNumbersToEnglish[seq];
		} else if (seq in brailleLettersToEnglish) {
			const letter = brailleLettersToEnglish[seq];
			output += capitalMode ? letter.toUpperCase() : letter;
		} else {
			throw new TranslatorError(`Unsupported braille sequence "${seq}"`);
		}

		// Only keep capital mode on for the next character once enabled
		capitalMode = seq === ControlSequences.CAPITAL;
	}

	return output;
}

// Translate an English string to Braille
function translateToBraille(englishStr: string) {
	let output = '';
	let numberMode = false;

	for (const char of englishStr) {
		if (char === ' ') {
			numberMode = false; // Spaces end number mode
			output += ControlSequences.SPACE;
		} else if (char in englishNumbersToBraille) {
			if (!numberMode) {
				output += ControlSequences.NUMBER;
				numberMode = true;
			}

			output += englishNumbersToBraille[char];
		} else if (char in englishLettersToBraille) {
			if (numberMode)
				throw new TranslatorError('Cannot output a letter while in number mode');

			output += englishLettersToBraille[char];
		} else {
			throw new TranslatorError(`Unsupported character "${char}"`);
		}
	}

	return output;
}

// Remove "ts-node" and "translator.ts" from the arguments
const input = process.argv.splice(2).join(' ');

const output = isBraille(input)
	? translateToEnglish(input)
	: translateToBraille(input);

console.log(output);
