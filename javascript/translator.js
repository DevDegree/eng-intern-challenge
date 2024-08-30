// braille -> alphabet
// alphabet -> braille

// Input: .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..
// Output: Abc 123

/**
 * .....O cap
 * O..... a
 * O.O... b
 * OO.... c
 * ...... space
 * .O.OOO number
 * O.O... 2
 * OO.... 3
 * OO.O.. 4
 */

// Input: 42
// Output: .O.OOOOO.O..O.O...

/**
 * .O.OOO number
 * OO.O.. 4
 * O.O... 2
 */

console.log("args", process.argv);
if (process.argv.length === 2) {
  console.error("Expected at least one argument!");
  process.exit(1);
}
const [_node, _script, ...params] = process.argv;

console.log("remaining args", params);
