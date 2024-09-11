import { argv } from 'process';
import converter from "./lib/converter";

const input = argv.slice(2).join(' ');
const output = converter.run(input);
console.log(output);
