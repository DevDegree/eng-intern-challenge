let t = "";
const regex = /^[.O]+$/;
let num_mode = false;
let Capital_mode = false;

const b_num = {};
b_num[".OOO.."] = "0";
b_num["O....."] = "1";
b_num["O.O..."] = "2";
b_num["OO...."] = "3";
b_num["OO.O.."] = "4";
b_num["O..O.."] = "5";
b_num["OOO..."] = "6";
b_num["OOOO.."] = "7";
b_num["O.OO.."] = "8";
b_num[".OO..."] = "9";

const b_atoz = {};
b_atoz["O....."] = "a";
b_atoz["O.O..."] = "b";
b_atoz["OO...."] = "c";
b_atoz["OO.O.."] = "d";
b_atoz["O..O.."] = "e";
b_atoz["OOO..."] = "f";
b_atoz["OOOO.."] = "g";
b_atoz["O.OO.."] = "h";
b_atoz[".OO..."] = "i";
b_atoz[".OOO.."] = "j";
b_atoz["O...O."] = "k";
b_atoz["O.O.O."] = "l";
b_atoz["OO..O."] = "m";
b_atoz["OO.OO."] = "n";
b_atoz["O..OO."] = "o";
b_atoz["OOO.O."] = "p";
b_atoz["OOOOO."] = "q";
b_atoz["O.OOO."] = "r";
b_atoz[".OO.O."] = "s";
b_atoz[".OOOO."] = "t";
b_atoz["O...OO"] = "u";
b_atoz["O.O.OO"] = "v";
b_atoz[".OOO.O"] = "w";
b_atoz["OO..OO"] = "x";
b_atoz["OO.OOO"] = "y";
b_atoz["O..OOO"] = "z";
b_atoz["......"] = " ";

const num_b = {};
num_b["0"] = ".OOO..";
num_b["1"] = "O.....";
num_b["2"] = "O.O...";
num_b["3"] = "OO....";
num_b["4"] = "OO.O..";
num_b["5"] = "O..O..";
num_b["6"] = "OOO...";
num_b["7"] = "OOOO..";
num_b["8"] = "O.OO..";
num_b["9"] = ".OO...";

const atoz_b = {};
atoz_b["a"] = "O.....";
atoz_b["b"] = "O.O...";
atoz_b["c"] = "OO....";
atoz_b["d"] = "OO.O..";
atoz_b["e"] = "O..O..";
atoz_b["f"] = "OOO...";
atoz_b["g"] = "OOOO..";
atoz_b["h"] = "O.OO..";
atoz_b["i"] = ".OO...";
atoz_b["j"] = ".OOO..";
atoz_b["k"] = "O...O.";
atoz_b["l"] = "O.O.O.";
atoz_b["m"] = "OO..O.";
atoz_b["n"] = "OO.OO.";
atoz_b["o"] = "O..OO.";
atoz_b["p"] = "OOO.O.";
atoz_b["q"] = "OOOOO.";
atoz_b["r"] = "O.OOO.";
atoz_b["s"] = ".OO.O.";
atoz_b["t"] = ".OOOO.";
atoz_b["u"] = "O...OO";
atoz_b["v"] = "O.O.OO";
atoz_b["w"] = ".OOO.O";
atoz_b["x"] = "OO..OO";
atoz_b["y"] = "OO.OOO";
atoz_b["z"] = "O..OOO";
atoz_b[" "] = "......";

const str = process.argv.slice(2).join(" ");

// const translator = (str) => {
// Braille -> string
if (str.length % 6 == 0 && regex.test(str)) {
  for (let i = 0; i < str.length; i += 6) {
    let letter = str.slice(i, i + 6);
    if (num_mode) {
      if (letter === "......") {
        t = t + " ";
        num_mode = false;
      } else if (b_num[letter]) {
        t = t + b_num[letter];
      }
    } else {
      if (letter == ".....O") {
        Capital_mode = true;
      } else if (letter == ".O.OOO") {
        num_mode = true;
      } else if (b_atoz[letter]) {
        if (Capital_mode) {
          t = t + b_atoz[letter].toUpperCase();
          Capital_mode = false;
        } else t = t + b_atoz[letter];
      }
    }
  }
  //   return t;
  console.log(t);
}
// String -> braille
else {
  for (let i = 0; i < str.length; i++) {
    if (!num_mode && str[i].match(/^[0-9]/)) {
      num_mode = true;
      t = t + ".O.OOO" + num_b[str[i]];
    } else if (str[i].match(/^[0-9]/)) {
      t = t + num_b[str[i]];
    } else if (str[i].match(/^[A-Z]/)) {
      if (num_mode) {
        t = t + "......";
        num_mode = false;
      }
      t = t + ".....O" + atoz_b[str[i].toLowerCase()];
    } else if (str[i].match(/^[a-z]/)) {
      if (num_mode) {
        t = t + "......";
        num_mode = false;
      }
      t = t + atoz_b[str[i]];
    } else if (str[i].match(/^[ ]/)) {
      if (num_mode) num_mode = false;
      t = t + "......";
    }
  }
  //   return t;
  console.log(t);
}
// };

// let str = ".O.OOOOO.O..O.O...";
// // str = ".O.OOOOO.O..O.O...AAAAAA";
// str =
//   ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
// str = "Hello world";
// str = "Hello 123";
// // str = ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..";
// str =
//   ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO";
// // str = ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....";

// document.getElementById("answer").textContent = translator(str);
