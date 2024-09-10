const process = require('process');

// Function to check if the input is Braille or English
function isBraille(input) {
  const braillePattern = /^[O.]+$/; // Braille will only contain 'O' and '.'
  return braillePattern.test(input);
}

// Main function to handle the input
function main() {
  // Get arguments from the command line
  const args = process.argv.slice(2); // Skip the first two elements (node and script path)

  if (args.length === 0) {
    console.error('Please provide a string to translate.');
    return;
  }

  const input = args.join(' '); // Combine all arguments into a single string

  // Determine if the input is Braille or English
  if (isBraille(input)) {
    console.log('Input is Braille');
  } else {
    console.log('Input is English');
  }
}

main();
