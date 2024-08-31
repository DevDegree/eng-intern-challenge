// Access the command-line arguments
const arg = process.argv.slice(2); // the first 2 arguments are reserved for the path to the executable & script file

///////////////// DO SOMETHING IF THE ARGUMENTS ARE NOT PROVIDED?? //////////////////

// Check if any arguments are provided
if (arg.length === 0) {
  //   console.log("No arguments provided. Please provide some arguments.");
  process.exit(1); // Exit with a non-zero status code to indicate an error
}

////////////////////////////// LOGIC //////////////

const [message] = arg; // the argument is the message provided in the command line, message is a string

// English to Braille mapping
const engToBraille = new Map();

engToBraille.set("a", "O.....");
engToBraille.set("b", "O.O...");
engToBraille.set("c", "OO....");
engToBraille.set("d", "OO.O..");
engToBraille.set("e", "O..O..");
engToBraille.set("f", "OOO...");
engToBraille.set("g", "OOOO..");
engToBraille.set("h", "O.OO..");
engToBraille.set("i", ".OO...");
engToBraille.set("j", ".OOO..");
engToBraille.set("k", "O...O.");
engToBraille.set("l", "O.O.O.");
engToBraille.set("m", "OO..O.");
engToBraille.set("n", "OO.OO.");
engToBraille.set("o", "O..OO.");
engToBraille.set("p", "OOO.O.");
engToBraille.set("q", "OOOOO.");
engToBraille.set("r", "O.OOO.");
engToBraille.set("s", ".OO.O.");
engToBraille.set("t", ".OOOO.");
engToBraille.set("u", "O...OO");
engToBraille.set("v", "O.O.OO");
engToBraille.set("w", ".OOO.O");
engToBraille.set("x", "OO..OO");
engToBraille.set("y", "OO.OOO");
engToBraille.set("z", "O..OOO");
engToBraille.set("capitalize", ".....O");
engToBraille.set("space", "......");
engToBraille.set("0", ".OOO..");
engToBraille.set("1", "O.....");
engToBraille.set("2", "O.O...");
engToBraille.set("3", "OO....");
engToBraille.set("4", "OO.O..");
engToBraille.set("5", "O..O..");
engToBraille.set("6", "OOO...");
engToBraille.set("7", "OOOO..");
engToBraille.set("8", "O.OO..");
engToBraille.set("9", ".OO...");

// Braille to English mapping
const brailleToEng = new Map();

brailleToEng.set("O.....", "a");
brailleToEng.set("O.O...", "b");
brailleToEng.set("OO....", "c");
brailleToEng.set("OO.O..", "d");
brailleToEng.set("O..O..", "e");
brailleToEng.set("OOO...", "f");
brailleToEng.set("OOOO..", "g");
brailleToEng.set("O.OO..", "h");
brailleToEng.set(".OO...", "i");
brailleToEng.set(".OOO..", "j");
brailleToEng.set("O...O.", "k");
brailleToEng.set("O.O.O.", "l");
brailleToEng.set("OO..O.", "m");
brailleToEng.set("OO.OO.", "n");
brailleToEng.set("O..OO.", "o");
brailleToEng.set("OOO.O.", "p");
brailleToEng.set("OOOOO.", "q");
brailleToEng.set("O.OOO.", "r");
brailleToEng.set(".OO.O.", "r");
brailleToEng.set(".OOOO.", "t");
brailleToEng.set("O...OO", "u");
brailleToEng.set("O.O.OO", "v");
brailleToEng.set(".OOO.O", "w");
brailleToEng.set("OO..OO", "x");
brailleToEng.set("OO.OOO", "y");
brailleToEng.set("O..OOO", "z");
brailleToEng.set(".....O", "capitalize");
brailleToEng.set("......", "space");
brailleToEng.set(".OOO..", "0");
brailleToEng.set("O.....", "1");
brailleToEng.set("O.O...", "2");
brailleToEng.set("OO....", "3");
brailleToEng.set("OO.O..", "4");
brailleToEng.set("O..O..", "5");
brailleToEng.set("OOO...", "6");
brailleToEng.set("OOOO..", "7");
brailleToEng.set("O.OO..", "8");
brailleToEng.set(".OO...", "9");

// 1. check if converting from braille to english or vice versa
if (message.split("").includes(".")) {
  // braille to english
}
