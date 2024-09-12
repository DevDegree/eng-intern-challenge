type TranslationMap = {
	characters: { [key: string]: string };
	digits: { [key: string]: string };
};

// The braille alphabet is a mapping of english characters and numbers to their corresponding braille dots
export const ENGLISH_TO_BRAILLE_MAP: TranslationMap = {
	characters: {
		a: "O.....",
		b: "O.O...",
		c: "OO....",
		d: "OO.O..",
		e: "O..O..",
		f: "OOO...",
		g: "OOOO..",
		h: "O.OO..",
		i: ".OO...",
		j: ".OOO..",
		k: "O...O.",
		l: "O.O.O.",
		m: "OO..O.",
		n: "OO.OO.",
		o: "O..OO.",
		p: "OOO.O.",
		q: "OOOOO.",
		r: "O.OOO.",
		s: ".OO.O.",
		t: ".OOOO.",
		u: "O...OO",
		v: "O.O.OO",
		w: ".OOO.O",
		x: "OO..OO",
		y: "OO.OOO",
		z: "O..OOO",
	},
	digits: {
		"1": "O.....",
		"2": "O.O...",
		"3": "OO....",
		"4": "OO.O..",
		"5": "O..O..",
		"6": "OOO...",
		"7": "OOOO..",
		"8": "O.OO..",
		"9": ".OO...",
		"0": ".OOO..",
	},
};

// Create a reverse map of the ENGLISH_TO_BRAILLE_MAP
export const BRAILLE_TO_ENGLISH_MAP: TranslationMap = {
	characters: Object.fromEntries(
		Object.entries(ENGLISH_TO_BRAILLE_MAP.characters).map(([k, v]) => [v, k]),
	),
	digits: Object.fromEntries(
		Object.entries(ENGLISH_TO_BRAILLE_MAP.digits).map(([k, v]) => [v, k]),
	),
};

export const SPECIAL_BRAILLE_INDICATORS = {
	capitalFollows: ".....O",
	numberFollows: ".O.OOO",
	space: "......", // Space is represented by 6 dots (empty matrix)
};
