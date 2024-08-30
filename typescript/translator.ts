const isValidBraille = (str: string): boolean => {
  const allowedSet: string[] = ["O", "."];

  for (const letter of str) {
    if (!allowedSet.includes(letter)) {
      return false;
    }
  }
  return true;
};

console.log(isValidBraille("..O...O...O"));

console.log(isValidBraille("......A...."));
