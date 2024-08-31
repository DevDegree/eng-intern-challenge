// Access the command-line arguments
const args = process.argv.slice(2); // the first 2 arguments are reserved for the path to the executable & script file

///////////////// DO SOMETHING IF THE ARGUMENTS ARE NOT PROVIDED?? //////////////////

// Check if any arguments are provided
if (args.length === 0) {
  //   console.log("No arguments provided. Please provide some arguments.");
  process.exit(1); // Exit with a non-zero status code to indicate an error
}

////////////////////////////// LOGIC //////////////

// Example of handling a specific argument
const [person] = args;
if (person) {
  console.log(`Hello, ${person}!`);
}
