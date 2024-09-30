const input = process.argv.slice(2).join(" ");

function isBraille(input) {
  for (let char of input) {
    if (char !== "." && char !== "O") {
      return false;
    }
  }

  return true;
}

