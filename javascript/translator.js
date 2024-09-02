#!/usr/bin/env node

const args = process.argv.slice(2);
if (args.length > 0) {
  console.log(args);
  console.log('Arguments provided:', args.join(', '));


} else {
  console.log('No arguments provided.');
}