# Rationale

- The `README.md` for language-specific instructions mentioned in the root `README.md` didn't have any content. So here's some notes on some questions I had along the way, and assumptions I made in lieu of them.

## Environment

Node version: 18.20.4

- Use of ESModule imports requires Node v13.2+
- To start program: `ts-node translator.ts`

## Questions

- Will inputs always be English OR Braille, or can it be a mix of both?
- Will inputs alway be a valid character? (e.g. for English: alphanumeric + spaces only, for Braille: . and O characters only)
- Will an input always be provided? (i.e. no argument passed into runtime)
- What lengths of input can be expected?
- Can there be consecutive capital or number prefixes in Braille input strings?
- Can there be consecutive spaces in Braille input strings?
- Can a capital or number prefix have no associated character? (i.e. trailing prefixes are allowed?)
- Should consecutive spaces in Braille be translated accurately into English? Or condensed into a single space?

## Assumptions

- Inputs will always be valid alphanumeric and space characters in English or Braille, not a mix of both
- An input will always be provided
- Expecting input lengths between 1 and 10,000
- Braille input strings will not contain consecutive number or capital prefixes
- Braille input strings may contain consecutive spaces, and the resulting English translation will have consecutive spaces
- Trailing capital or number prefixes will be omitted from the translated string

- Error handling exists for inputs that violates any above assumed criteria

## Notes

- The "legend" objects that map individual characters to their respective translated ones were used with the trade-off of additional space requirements, but less time taken to translate at runtime.

- I chose procedural approach over other paradigms (e.g. OOP, FP) because of the simplicity of the program. Entities were somewhat vague and the interactions were not complex.

- I pondered on whether or not the error handling was too much for the multiple consecutive Braille prefixes edge case, but decided that it was better to constrain the user so that the behavior of the program is predictable to them.

If, for example, we allowed for consecutive prefixes for capitals, would the user expect that the next multiple letters are capitalized? Or just a single one? Depending on their expectation, the user experience could take a hit. This ambiguity was what led to my decision.

- `translator.test.ts` should not be edited, but based on the testing command being `jest`, I assume that any other jest test files I create will also be executed and may interfere with the automated checking of my application. I got around this by renaming my `.test.ts` file to a simple `.ts` file for the PR so that it wouldn't be caught by the `jest` command.

- Fun time! Thanks for the consideration!
