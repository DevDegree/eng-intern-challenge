import charMap from "./charMap";
import brailleMap from "./brailleMap";

function translator(word: string): string {
	let regexp: RegExp = /\b(?!\w*[.O])\w+\b/;

	if (regexp.test(word)) {
		return translateToBraille(word);
	} else {
		return translateToEnglish(word);
	}
}

function translateToBraille(word: string): string {
	let output: string = "";

	const numStr: string = "1234567890";
	let i: number = 0;

	while (i < word.length) {
		const char: string = word[i];
		const translation: string | undefined = charMap.get(word[i].toLowerCase());

		if (numStr.includes(char)) {
			if (i == 0 || !numStr.includes(word[i - 1])) {
				output += ".O.OOO";
			}
		} else if (word.charCodeAt(i) > 64 && word.charCodeAt(i) < 91) {
			output += ".....O";
		}

		output += translation;
		i += 1;
	}
	console.log(output);
	return output;
}

function translateToEnglish(word: string): string {
	let output: string = "";

	while (word.length > 0) {
		let brailleChar: string = word.slice(0, 6);
		let translation: string | undefined;

		if (brailleChar == ".O...O") {
			word = word.slice(6);
			continue;
		}

		if (brailleChar == ".O.OOO") {
			word = word.slice(6);

			while (word.length > 0) {
				brailleChar = word.slice(0, 6);

				if (brailleChar == "......") {
					break;
				}

				translation = brailleMap.get("n" + brailleChar);
				output += translation;

				word = word.slice(6);
			}

			output += " ";
			word = word.slice(6);
		} else if (brailleChar == ".....O") {
			brailleChar = word.slice(6, 12);
			translation = brailleMap.get(brailleChar)?.toUpperCase();
			output += translation;
			word = word.slice(12);
		} else {
			translation = brailleMap.get(brailleChar);
			output += translation;
			word = word.slice(6);
		}
	}
	console.log(output);
	return output;
}

if (require.main === module) {
	const args = process.argv.slice(2);
	const input = args.join(" ");
	translator(input);
}
