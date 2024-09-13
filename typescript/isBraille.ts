export default function isBraille(str: string): boolean {
  if (str.length !== 6) {
    return false;
  }

  for (let char of str) {
    if (!(char == "o" || char == ".")) {
      return false;
    }
  }

  return true;
}
