const isBraille = (string) => {
  if (string.length === 0) return false;
  const normalizedString = string.toUpperCase();
  const allowableCharacters = ["O", "."];
  for (let index = 0; index < normalizedString.length; index++) {
    const element = normalizedString[index];
    if (!allowableCharacters.includes(element)) return false;
  }
  return true;
};

module.exports = { isBraille };
