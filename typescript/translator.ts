function doStuff(args: string[]) {
  const concatenatedArgs = args.join(" ");

  console.log(concatenatedArgs);
}

function main() {
  const args = process.argv.slice(2);

  console.log(args);

  if (args.length === 0) {
    console.error("Error: No input specified.");
    process.exit(1);
  }

  doStuff(args);
}

main();
