export const isValidEnglish = (input) => {
  // Regular expression to match only lowercase letters, uppercase letters, numbers, and spaces
  const validEnglishPattern = /^[a-zA-Z0-9\s]*$/;

  return validEnglishPattern.test(input);
};
