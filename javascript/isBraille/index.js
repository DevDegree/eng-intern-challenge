
// Function that checks if a string passed, is a braille string or a regular one.
const isBraille = string => {
  // if string is not divisble by 6, then it cannot be a true brailie string.
  if (string.length % 6 > 0) return false;
  
  // if string does not contain combinations of . symbol and O symbol, then its not a brailie.
  if (!(/^[.O]+$/.test(string))) return false;

  return true;
}

module.exports = isBraille;
