// Comannd Line Arguments: node translator.ts "Hello World"
const [, , ...args] = process.argv;
const input = args.join(" ");
console.log(process.argv.slice(2)); // [ '--build', '--test-args', 'TestArgument1' ]
