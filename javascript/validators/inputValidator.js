export default function inputChecker(input) {
  const regex = /^[O.]+$/;

  // if args is divisible by 6 and contains only "O" or ".", it's braille
  if (input % 6 === 0 && str.match(regex) !== null) {
    return 'braille';
  }

  return 'alphanumeric';
}
