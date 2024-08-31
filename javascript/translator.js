// Access the command-line arguments
const arg = process.argv.slice(2); // the first 2 arguments are reserved for the path to the executable & script file

///////////////// DO SOMETHING IF THE ARGUMENTS ARE NOT PROVIDED?? //////////////////

// Check if any arguments are provided
if (arg.length === 0 || arg === null) {
  //   console.log("No arguments provided. Please provide some arguments.");
  // process.exit(1); // Exit with a non-zero status code to indicate an error
  // console.log(error);
}

////////////////////////////// LOGIC //////////////

const message = arg.join(" "); // the argument is the message provided in the command line, message is a string

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
engToBraille.set(" ", "......");
engToBraille.set("number follows", ".O.OOO");
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

brailleToEng.set("O.....", ["a", "1"]);
brailleToEng.set("O.O...", ["b", "2"]);
brailleToEng.set("OO....", ["c", "3"]);
brailleToEng.set("OO.O..", ["d", "4"]);
brailleToEng.set("O..O..", ["e", "5"]);
brailleToEng.set("OOO...", ["f", "6"]);
brailleToEng.set("OOOO..", ["g", "7"]);
brailleToEng.set("O.OO..", ["h", "8"]);
brailleToEng.set(".OO...", ["i", "9"]);
brailleToEng.set(".OOO..", ["j", "0"]);
brailleToEng.set("O...O.", ["k"]);
brailleToEng.set("O.O.O.", ["l"]);
brailleToEng.set("OO..O.", ["m"]);
brailleToEng.set("OO.OO.", ["n"]);
brailleToEng.set("O..OO.", ["o"]);
brailleToEng.set("OOO.O.", ["p"]);
brailleToEng.set("OOOOO.", ["q"]);
brailleToEng.set("O.OOO.", ["r"]);
brailleToEng.set(".OO.O.", ["s"]);
brailleToEng.set(".OOOO.", ["t"]);
brailleToEng.set("O...OO", ["u"]);
brailleToEng.set("O.O.OO", ["v"]);
brailleToEng.set(".OOO.O", ["w"]);
brailleToEng.set("OO..OO", ["x"]);
brailleToEng.set("OO.OOO", ["y"]);
brailleToEng.set("O..OOO", ["z"]);
brailleToEng.set(".....O", ["capitalize"]);
brailleToEng.set("......", [" "]);
brailleToEng.set(".O.OOO", ["number follows"]);
// brailleToEng.set(".OOO..", "0");
// brailleToEng.set("O.....", "1");
// brailleToEng.set("O.O...", "2");
// brailleToEng.set("OO....", "3");
// brailleToEng.set("OO.O..", "4");
// brailleToEng.set("O..O..", "5");
// brailleToEng.set("OOO...", "6");
// brailleToEng.set("OOOO..", "7");
// brailleToEng.set("O.OO..", "8");
// brailleToEng.set(".OO...", "9");

// console.log(typeof message);
// console.log(message.slice(6, 12));
// console.log(brailleToEng.get(message.slice(6, 12))[0].toUpperCase());

let res = "";

if (message.split("").includes(".")) {
  // 1. check if converting from braille to english or vice versa
  // braille to english
  for (let i = 0; i < message.length; i += 6) {
    // 6 chars = 1 braille char
    if (brailleToEng.get(message.slice(i, i + 6))[0] === "capitalize") {
      res += brailleToEng.get(message.slice(i + 6, i + 12))[0].toUpperCase();
      i += 12;
      // console.log(res);
    }
    if (brailleToEng.get(message.slice(i, i + 6))[0] === "number follows") {
      while (
        i < message.length &&
        brailleToEng.get(message.slice(i, i + 6))[0] !== " "
      ) {
        res += brailleToEng.get(message.slice(i, i + 6))[1] || "";
        i += 6;
        // console.log(res);
      }
      if (i !== message.length) res += " ";
      // res += " ";
      // i += 6;
      // console.log(res);
    } else {
      res += brailleToEng.get(message.slice(i, i + 6))[0];
      // console.log(res);
    }
  }
} else {
  // braille to english translation logic
  for (let i = 0; i < message.length; i++) {
    // console.log(i);
    // console.log(res);
    if (
      message[i] === message[i].toUpperCase() &&
      !/[0123456789 ]/.test(message[i])
    ) {
      // console.log(message[i]);
      // console.log(res);
      res +=
        engToBraille.get("capitalize") +
        engToBraille.get(message[i].toLowerCase());
      i++;
      // console.log(message[i]);
      // console.log(res);
    }
    if (/[0123456789]/.test(message[i])) {
      // console.log(message[i]);
      res += engToBraille.get("number follows");
      while (i < message.length && message[i] !== " ") {
        // console.log(message[i]);
        res += engToBraille.get(message[i]);
        i++;
      }
      // i++;
      // if (i !== message.length - 1) res += engToBraille.get(" ");
      if (i !== message.length) res += engToBraille.get(" ");
    } else {
      // console.log(message[i]);
      res += engToBraille.get(message[i]);
      // console.log(i);
      // console.log(res);
    }
    //   console.log(i);
    //   console.log(res);
  }
}

console.log(res);

////////////////// TESTS ////////////

// console.log([res]);

// HELLO WORLD
// console.log(
//   res ===
//     ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
// ); // Hello world
// console.log(res === "Hello world");

// 42
// console.log(res === ".O.OOOOO.O..O.O..."); // 42
// console.log(res === "42");

// ABC 123
// console.log(res === ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."); // Abc 123
// console.log(res === "Abc 123");

// ABC 123 XYZ
// console.log(
//   res ===
//     ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
// ); // Abc 123 xYz
// console.log(res === "Abc 123 xYz");
