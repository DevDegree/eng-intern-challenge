let userInput = process.argv.slice(2).join(" ");

if (userInput.includes(".")) {
	console.log(bToE());
}
else { 
	console.log(eToB());
}

function bToE() {

	let translationOutput = '';
	let currentChar;
	let numberFollows = false;
	let capitalizeNext = false;

	for (i = 0; i < userInput.length; i += 6) {
		currentChar = userInput.substring(i, i + 6);

		switch (currentChar) {
			case "O.....":
				if (capitalizeNext) {
					translationOutput += "A";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "1";
				} else {
					translationOutput += "a";
				}
				break;

			case "O.O...":
				if (capitalizeNext) {
					translationOutput += "B";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "2";
				} else {
					translationOutput += "b";
				}
				break;

			case "OO....":
				if (capitalizeNext) {
					translationOutput += "C";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "3";
				} else {
					translationOutput += "c";
				}
				break;

			case "OO.O..":
				if (capitalizeNext) {
					translationOutput += "D";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "4";
				} else {
					translationOutput += "d";
				}
				break;

			case "O..O..":
				if (capitalizeNext) {
					translationOutput += "E";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "5";
				} else {
					translationOutput += "e";
				}
				break;

			case "OOO...":
				if (capitalizeNext) {
					translationOutput += "F";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "6";
				} else {
					translationOutput += "f";
				}
				break;

			case "OOOO..":
				if (capitalizeNext) {
					translationOutput += "G";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "7";
				} else {
					translationOutput += "g";
				}
				break;

			case "O.OO..":
				if (capitalizeNext) {
					translationOutput += "H";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "8";
				} else {
					translationOutput += "h";
				}
				break;

			case ".OO...":
				if (capitalizeNext) {
					translationOutput += "I";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "9";
				} else {
					translationOutput += "i";
				}
				break;

			case ".OOO..":
				if (capitalizeNext) {
					translationOutput += "J";
					capitalizeNext = false;
				} else if (numberFollows) {
					translationOutput += "0";
				} else {
					translationOutput += "j";
				}
				break;

			case "O...O.":
				translationOutput += capitalizeNext ? "K" : "k";
				capitalizeNext = false;
				break;

			case "O.O.O.":
				translationOutput += capitalizeNext ? "L" : "l";
				capitalizeNext = false;
				break;

			case "OO..O.":
				translationOutput += capitalizeNext ? "M" : "m";
				capitalizeNext = false;
				break;

			case "OO.OO.":
				translationOutput += capitalizeNext ? "N" : "n";
				capitalizeNext = false;
				break;

			case "O..OO.":
				translationOutput += capitalizeNext ? "O" : "o";
				capitalizeNext = false;
				break;

			case "OOO.O.":
				translationOutput += capitalizeNext ? "P" : "p";
				capitalizeNext = false;
				break;

			case "OOOOO.":
				translationOutput += capitalizeNext ? "Q" : "q";
				capitalizeNext = false;
				break;

			case "O.OOO.":
				translationOutput += capitalizeNext ? "R" : "r";
				capitalizeNext = false;
				break;

			case ".OO.O.":
				translationOutput += capitalizeNext ? "S" : "s";
				capitalizeNext = false;
				break;

			case ".OOOO.":
				translationOutput += capitalizeNext ? "T" : "t";
				capitalizeNext = false;
				break;

			case "O...OO":
				translationOutput += capitalizeNext ? "U" : "u";
				capitalizeNext = false;
				break;

			case "O.O.OO":
				translationOutput += capitalizeNext ? "V" : "v";
				capitalizeNext = false;
				break;

			case ".OOO.O":
				translationOutput += capitalizeNext ? "W" : "w";
				capitalizeNext = false;
				break;

			case "OO..OO":
				translationOutput += capitalizeNext ? "X" : "x";
				capitalizeNext = false;
				break;

			case "OO.OOO":
				translationOutput += capitalizeNext ? "Y" : "y";
				capitalizeNext = false;
				break;

			case "O..OOO":
				translationOutput += capitalizeNext ? "Z" : "z";
				capitalizeNext = false;
				break;

			case ".....O":
				capitalizeNext = true;
				break;

			case ".O.OOO":
				numberFollows = true;
				break;

			case "......":
				translationOutput += " ";
				break;
		}
	}
	return translationOutput;
}

function eToB() {

	let translationOutput = '';
	let currentChar;
	let numberFollows = true;

	for (i = 0; i < userInput.length; i++) {
		currentChar = userInput[i];


		switch (currentChar) {
			case "a":
				translationOutput += "O.....";
				break;

			case "A":
				translationOutput += ".....O" + "O.....";
				break;

			case "1":
				translationOutput += numberFollows ? ".O.OOO" + "O....." : "O.....";
				numberFollows = false;
				break;

			case "b":
				translationOutput += "O.O...";
				break;

			case "B":
				translationOutput += ".....O" + "O.O...";
				break;

			case "2":
				translationOutput += numberFollows ? ".O.OOO" + "O.O..." : "O.O...";
				numberFollows = false;
				break;

			case "c":
				translationOutput += "OO....";
				break;

			case "C":
				translationOutput += ".....O" + "OO....";
				break;

			case "3":
				translationOutput += numberFollows ? ".O.OOO" + "OO...." : "OO....";
				numberFollows = false;
				break;

			case "d":
				translationOutput += "OO.O..";
				break;

			case "D":
				translationOutput += ".....O" + "OO.O..";
				break;

			case "4":
				translationOutput += numberFollows ? ".O.OOO" + "OO.O.." : "OO.O..";
				numberFollows = false;
				break;

			case "e":
				translationOutput += "O..O..";
				break;

			case "E":
				translationOutput += ".....O" + "O..O..";
				break;

			case "5":
				translationOutput += numberFollows ? ".O.OOO" + "O..O.." : "O..O..";
				numberFollows = false;
				break;

			case "f":
				translationOutput += "OOO...";
				break;

			case "F":
				translationOutput += ".....O" + "OOO...";
				break;

			case "6":
				translationOutput += numberFollows ? ".O.OOO" + "OOO..." : "OOO...";
				numberFollows = false;
				break;

			case "g":
				translationOutput += "OOOO..";
				break;

			case "G":
				translationOutput += ".....O" + "OOOO..";
				break;

			case "7":
				translationOutput += numberFollows ? ".O.OOO" + "OOOO.." : "OOOO..";
				numberFollows = false;
				break;

			case "h":
				translationOutput += "O.OO..";
				break;

			case "H":
				translationOutput += ".....O" + "O.OO..";
				break;

			case "8":
				translationOutput += numberFollows ? ".O.OOO" + "O.OO.." : "O.OO..";
				numberFollows = false;
				break;

			case "i":
				translationOutput += ".OO...";
				break;

			case "I":
				translationOutput += ".....O" + ".OO...";
				break;

			case "9":
				translationOutput += numberFollows ? ".O.OOO" + ".OO..." : ".OO...";
				numberFollows = false;
				break;

			case "j":
				translationOutput += ".OOO..";
				break;

			case "J":
				translationOutput += ".....O" + ".OOO..";
				break;

			case "0":
				translationOutput += numberFollows ? ".O.OOO" + ".OOO.." : ".OOO..";
				numberFollows = false;
				break;

			case "k":
				translationOutput += "O...O.";
				break;

			case "K":
				translationOutput += ".....O" + "O...O.";
				break;

			case "l":
				translationOutput += "O.O.O.";
				break;

			case "L":
				translationOutput += ".....O" + "O.O.O.";
				break;

			case "m":
				translationOutput += "OO..O.";
				break;

			case "M":
				translationOutput += ".....O" + "OO..O.";
				break;

			case "n":
				translationOutput += "OO.OO.";
				break;

			case "N":
				translationOutput += ".....O" + "OO.OO.";
				break;

			case "o":
				translationOutput += "O..OO.";
				break;

			case "O":
				translationOutput += ".....O" + "O..OO.";
				break;

			case "p":
				translationOutput += "OOO.O.";
				break;

			case "P":
				translationOutput += ".....O" + "OOO.O.";
				break;

			case "q":
				translationOutput += "OOOOO.";
				break;

			case "Q":
				translationOutput += ".....O" + "OOOOO.";
				break;

			case "r":
				translationOutput += "O.OOO.";
				break;

			case "R":
				translationOutput += ".....O" + "O.OOO.";
				break;

			case "s":
				translationOutput += ".OO.O.";
				break;

			case "S":
				translationOutput += ".....O" + ".OO.O.";
				break;

			case "t":
				translationOutput += ".OOOO.";
				break;

			case "T":
				translationOutput += ".....O" + ".OOOO.";
				break;

			case "u":
				translationOutput += "O...OO";
				break;

			case "U":
				translationOutput += ".....O" + "O...OO";
				break;

			case "v":
				translationOutput += "O.O.OO";
				break;

			case "V":
				translationOutput += ".....O" + "O.O.OO";
				break;

			case "w":
				translationOutput += ".OOO.O";
				break;

			case "W":
				translationOutput += ".....O" + ".OOO.O";
				break;

			case "x":
				translationOutput += "OO..OO";
				break;

			case "X":
				translationOutput += ".....O" + "OO..OO";
				break;

			case "y":
				translationOutput += "OO.OOO";
				break;

			case "Y":
				translationOutput += ".....O" + "OO.OOO";
				break;

			case "z":
				translationOutput += "O..OOO";
				break;

			case "Z":
				translationOutput += ".....O" + "O..OOO";
				break;

			case " ":
				translationOutput += "......";
				numberFollows = true;
				break;
		}
	}
	return translationOutput;
}
