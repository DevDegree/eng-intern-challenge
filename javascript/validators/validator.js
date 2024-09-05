export default function validator(input) {
  const regex = /^[O.]+$/;

  // if args is divisible by 6 and contains only "O" or ".", it's braille
  if (input.length % 6 === 0 && input.match(regex) !== null) {
    return 'braille';
  }

  // otherwise, it's alphanumeric
  return 'alphanumeric';
}

// stretch
// return an error message if arguments contain invalid characters
// if argument is braille and contains characters other than "O" or ".", and if argument is not divisible by 6, return an error message
// if argument is english and contains characters other than letters, numbers, or space, return an error message
