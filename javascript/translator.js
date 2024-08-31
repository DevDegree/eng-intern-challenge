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

// 1. check if converting from braille to english or vice versa
if (message.split("")[0] === ".") {
  // braille to english
  console.log(engToBraille.get("a"));
}
