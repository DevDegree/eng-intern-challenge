const input = '42';
let output;

if (input.includes('.')) {
  output = 'Braille';
} else {
  output = 'English';
}

console.log(output);