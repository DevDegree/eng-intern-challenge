const {
  translateBrailleToEnglish,
  isBraille,
  translateEnglishToBraille,
} = require("./helpers");

const [_node, _script, ...args] = process.argv;

const argsAsString = args.join(" ");
const processedArgs = argsAsString.trim();

let output = "";
if (isBraille(processedArgs)) {
  output = translateBrailleToEnglish(processedArgs);
} else {
  output = translateEnglishToBraille(processedArgs);
}

console.log(output);
