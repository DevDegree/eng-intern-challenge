/**
 * check if a string is or isn't valid Braille such that it only contains O or .
 *
 * @example
 * // returns false
 * isValidBraille("..O...O...A.")
 *
 * @returns {boolean} Returns whether or not it is a braille string
 */
const isValidBraille = (str: string): boolean => {
  const allowedSet: string[] = ["O", "."];

  for (const letter of str) {
    if (!allowedSet.includes(letter)) {
      return false;
    }
  }
  return true;
};

const clArgs = process.argv.slice(2).join(" ");

// if true -> translate to braille
// if false -> translate to english
console.log(isValidBraille(clArgs));
