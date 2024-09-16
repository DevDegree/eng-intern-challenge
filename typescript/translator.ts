class BrailleTranslator {
	private lettersMap: { [key: string]: string };
	private numbersMap: { [key: string]: string };
	constructor() {
		// lettersMap maps both English letters -> Braille and Braille -> English
		this.lettersMap = {
			a: 'O.....',
			b: 'O.O...',
			c: 'OO....',
			d: 'OO.O..',
			e: 'O..O..',
			f: 'OOO...',
			g: 'OOOO..',
			h: 'O.OO..',
			i: '.OO...',
			j: '.OOO..',
			k: 'O...O.',
			l: 'O.O.O.',
			m: 'OO..O.',
			n: 'OO.OO.',
			o: 'O..OO.',
			p: 'OOO.O.',
			q: 'OOOOO.',
			r: 'O.OOO.',
			s: '.OO.O.',
			t: '.OOOO.',
			u: 'O...OO',
			v: 'O.O.OO',
			w: '.OOO.O',
			x: 'OO..OO',
			y: 'OO.OOO',
			z: 'O..OOO',
			CAPITAL: '.....O',
			NUMBER: '.O.OOO',
			' ': '......',
		};
		this.numbersMap = {
			1: 'O.....',
			2: 'O.O...',
			3: 'OO....',
			4: 'OO.O..',
			5: 'O..O..',
			6: 'OOO...',
			7: 'OOOO..',
			8: 'O.OO..',
			9: '.OO...',
			0: '.OOO..',
			DECIMAL: '.O...O',
			' ': '......',
			// both 'o' and '>' have the same Braille representation
			// the instructions are not clear on how to handle this case
			'.': '..OO.O',
			',': '..O...',
			'?': '..O.OO',
			'!': '..OOO.',
			':': '..OO..',
			';': '..O.O.',
			'-': '....OO',
			'/': '.O..O.',
			'<': '.OO..O',
			'>': 'O..OO.',
			'(': 'O.O..O',
			')': '.O.OO.',
		};

		Object.entries(this.lettersMap).forEach(
			([key, value]) => (this.lettersMap[value] = key)
		);
		Object.entries(this.numbersMap).forEach(
			([key, value]) => (this.numbersMap[value] = key)
		);
	}

	/**
	 * Translates the given text to Braille.
	 *
	 * @param text - The text to be translated.
	 * @returns The Braille representation of the text.
	 */
	translateToBraille(text: string): string {
		let res = '';
		let index = 0;
		while (index < text.length) {
			const char = text[index];
			if (this.isNumber(char)) {
				res += this.lettersMap['NUMBER'];
				res += this.numbersMap[char];
				index++;

				while (
					index < text.length &&
					(this.isNumber(text[index]) || text[index] === '.')
				) {
					res += this.numbersMap[text[index]];
					index++;
				}
			} else {
				if (char !== ' ' && char === char.toUpperCase()) {
					res += this.lettersMap['CAPITAL'];
				}
				res += this.lettersMap[char.toLowerCase()];
				index++;
			}
		}
		return res;
	}

	/**
	 * Translates the given text to English.
	 *
	 * @param text - The text to be translated.
	 * @returns The translated text in English, or null if the translation failed.
	 */
	translateToEnglish(text: string): string | null {
		// split text into group of 6 characters
		const characters = text.match(/.{1,6}/g) as string[];

		let result = '';
		let capitalFollows = false;
		let numberFollows = false;
		for (const char of characters) {
			if (!numberFollows) {
				// use lettersMap
				const c = this.lettersMap[char];
				if (!c) {
					// if there's no corresponding character, return null to indicate that the translation failed
					return null;
				}

				// special cases
				if (c === 'CAPITAL') {
					capitalFollows = true;
					continue;
				} else if (c === 'NUMBER') {
					numberFollows = true;
					continue;
				}

				// otherwise append the character
				if (capitalFollows) {
					result += c.toUpperCase();
					capitalFollows = false;
				} else {
					result += c;
				}
			} else {
				// use numbersMap
				const c = this.numbersMap[char];
				if (!c) {
					return null;
				}

				if (c === 'DECIMAL') {
					result += '.';
				} else {
					result += c;
					if (c === ' ') {
						// if c is ' ' then we can reset the numberFollows flag
						numberFollows = false;
					}
				}
			}
		}

		return result;
	}

	/**
	 * Determines if the given text is probably in Braille.
	 *
	 * @param text - The text to check.
	 * @returns A boolean indicating whether the text is probably in Braille.
	 */
	probablyBraille(text: string): boolean {
		return text.length % 6 === 0 && text.match(/[^O.]/) === null;
	}

	private isNumber(c: string): boolean {
		return '1234567890'.includes(c);
	}
}

const main = (input: string): string => {
	// @ts-ignore
	const translator = new BrailleTranslator();

	const probablyBraille = translator.probablyBraille(input);
	if (probablyBraille) {
		// try to translate to English
		const translatedEnglish = translator.translateToEnglish(input);

		if (translatedEnglish) {
			return translatedEnglish;
		}

		const translatedBraille = translator.translateToBraille(input);
		return translatedBraille;
	} else {
		// translate to Braille
		const translatedBraille = translator.translateToBraille(input);
		return translatedBraille;
	}
};

// @ts-ignore
console.log(main(process.argv.slice(2).join(' ')));

// Test cases
// console.assert(
// 	main('Hello world') ===
// 		'.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..',
// 	'Test 1'
// );
// console.assert(main('42') === '.O.OOOOO.O..O.O...', 'Test 2');
// console.assert(main(main('42.7')) === '42.7', 'Test 3');
// console.assert(main(main('Abc 123')) === 'Abc 123', 'Test 4');
// console.assert(
// 	main(main('Hello World 1 2 3')) === 'Hello World 1 2 3',
// 	'Test 5'
// );
