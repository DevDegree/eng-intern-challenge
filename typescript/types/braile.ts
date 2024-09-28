const brailleMap = new Map<string, string>([
	["a", "O....."], ["b", "O.O..."], ["c", "OO...."], ["d", "OO.O.."], ["e", "O..O.."],
	["f", "OOO..."], ["g", "OOOO.."], ["h", "O.OO.."], ["i", ".OO..."], ["j", ".OOO.."],
	["k", "O...O."], ["l", "O.O.O."], ["m", "OO..O."], ["n", "OO.OO."], ["o", "O..OO."],
	["p", "OOO.O."], ["q", "OOOOO."], ["r", "O.OOO."], ["s", ".OO.O."], ["t", ".OOOO."],
	["u", "O...OO"], ["v", "O.O.OO"], ["w", ".OOO.O"], ["x", "OO..OO"], ["y", "OO.OOO"], 
	["z", "O..OOO"],
	["1", "O....."], ["2", "O.O..."], ["3", "OO...."], ["4", "OO.O.."], ["5", "O..O.."],
	["6", "OOO..."], ["7", "OOOO.."], ["8", "O.OO.."], ["9", ".OO..."], ["0", ".OOO.."],
	["capital", ".....O"], ["number", ".O.OOO"], ["decimal", ".O...O"],
	[" ", "......"], [".", "..OO.O"], [",", "..O..."], ["?", "..O.OO"], ["!", "..OOO."], 
	[":", "..OO.."], [";", "..O.O."], ["-", "....OO"], ["/", ".O..O."], ["<", ".OO..O"], 
	[">", "O..OO."], ["(", "O.O..O"], [")", ".O.OO."]
]);

const alphabetReverseMap = new Map<string, string>();
const numbersReverseMap = new Map<string, string>();
const specialCharReverseMap = new Map<string, string>();

brailleMap.forEach((value, key) => {
	/[a-z]/.test(key) &&
	alphabetReverseMap.set(value, key);
});
brailleMap.forEach((value, key) => {
	/[0-9]/.test(key) &&
	numbersReverseMap.set(value, key);
});
brailleMap.forEach((value, key) => {
	!/[a-z0-9]/.test(key) &&
	specialCharReverseMap.set(value, key);
});

export function translateBrailleToEnglish(braille: string): string {
	let english = "";
	let isNumber = false;
	const brailleChars = braille.match(/.{1,6}/g) || [];
  	let isCapital = false;

	brailleChars.forEach((brailleChar) => {
		if(brailleChar === brailleMap.get("capital")){
			isCapital = true;
			return;
		}
		if(brailleChar === brailleMap.get("number")){
			isNumber = true;
			return;
		}
		if(brailleChar === brailleMap.get("decimal")){
			english += ".";
			return;
		}
		if(brailleChar === brailleMap.get(" ")){
			english += " ";
			return;
		}

		if(isCapital){
			english += alphabetReverseMap.get(brailleChar).toUpperCase() || "";
			isCapital = false;
			return;
		}else if(isNumber){
			english += numbersReverseMap.get(brailleChar) || "";
			isNumber = false;
			return;
		}else{
			english += alphabetReverseMap.get(brailleChar)|| "";
		}
		
	});
	return english;
}
