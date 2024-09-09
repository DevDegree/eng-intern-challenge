const brailleToTextArray = {
	"o.....": "a",
	"o.o...": "b",
	"oo....": "c",
	"oo.o..": "d",
	"o..o..": "e",
	"ooo...": "f",
	"oooo..": "g",
	"o.oo..": "h",
	".oo...": "i",
	".ooo..": "j",
	"o...o.": "k",
	"o.o.o.": "l",
	"oo..o.": "m",
	"oo.oo.": "n",
	"o..oo.": "o",
	"ooo.o.": "p",
	"ooooo.": "q",
	"o.ooo.": "r",
	".oo.o.": "s",
	".oooo.": "t",
	"o...oo": "u",
	"o.o.oo": "v",
	".ooo.o": "w",
	"oo..oo": "x",
	"oo.ooo": "y",
	"o..ooo": "z",
	"......": " ",
	".....o": "capital",
	"....oo": "number",
};

const textToBrailleArray = {
	a: "o.....",
	b: "o.o...",
	c: "oo....",
	d: "oo.o..",
	e: "o..o..",
	f: "ooo...",
	g: "oooo..",
	h: "o.oo..",
	i: ".oo...",
	j: ".ooo..",
	k: "o...o.",
	l: "o.o.o.",
	m: "oo..o.",
	n: "oo.oo.",
	o: "o..oo.",
	p: "ooo.o.",
	q: "ooooo.",
	r: "o.ooo.",
	s: ".oo.o.",
	t: ".oooo.",
	u: "o...oo",
	v: "o.o.oo",
	w: ".ooo.o",
	x: "oo..oo",
	y: "oo.ooo",
	z: "o..ooo",
	" ": "......",
	1: "o.....",
	2: "o.o...",
	3: "oo....",
	4: "oo.o..",
	5: "o..o..",
	6: "ooo...",
	7: "oooo..",
	8: "o.oo..",
	9: ".oo...",
	0: ".ooo..",
};

function translate(input) {
	const isBraille = /^[o. ]+$/.test(input);
	let capitalizeNext = false;
	let numberMode = false;

	if (isBraille) {
		// Braille to text
		return input
			.split(" ")
			.map((braille) => {
				if (braille === ".....o") {
					capitalizeNext = true;
					return ""; //Accounts for capitalization
				}
				if (braille === "....oo") {
					numberMode = true;
					return ""; // Accounts for numbers
				}
				let letter = brailleToTextArray[braille] || "";
				if (capitalizeNext) {
					letter = letter.toUpperCase();
					capitalizeNext = false;
				}
				if (numberMode && /[a-z]/.test(letter)) {
					letter = String.fromCharCode(letter.charCodeAt(0) - 49);
				}
				if (!/[0-9]/.test(letter)) {
					numberMode = false;
				}
				return letter;
			})
			.join("");
	} else {
		// Text to braille
		return input
			.split("")
			.map((char) => {
				if (/[A-Z]/.test(char)) {
					return ".....o " + textToBrailleArray[char.toLowerCase()];
				}
				if (/[0-9]/.test(char)) {
					return "....oo " + textToBrailleArray[char];
				}
				return textToBrailleArray[char.toLowerCase()] || "";
			})
			.join(" ");
	}
}

console.log(translate(process.argv[2] || "Put translation in here"));
