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
- Should consecutive spaces in Braille be translated accurately into English? Or condensed into a single space?

## Assumptions

- Inputs will always be valid alphanumeric and space characters in English or Braille, not a mix of both
- An input will always be provided
- Expecting input lengths between 1 and 10,000
- Braille input strings will not contain consecutive number or capital prefixes
- Braille input strings may contain consecutive spaces, and the resulting English translation will have consecutive spaces

- Error handling exists for inputs that violates any above assumed criteria

## Notes

- The "legend" objects that map individual characters to their respective translated ones were used with the trade-off of additional space requirements, but less time taken to translate at runtime.

- Fun time! Thanks for the consideration!
