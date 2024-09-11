# JavaScript Instructions

This document provides a brief overview of a command-line application that enables users to translate English to Braille and vice versa.

Each English letter, number and punctuation is represented by a specific combination of six dots, usually arranged in a rectangle of two columns of three dots. Within this command-line application, Braille is represented by combinations of `O` and `.`, with `O` representing a raised dot.

## Getting Started
### Installation
This application requires Node.js to run. After this prerequisite is met, the application can be installed with the command-line:
```
npm install
```

### Run the Code
Once installed, the application can be run using:
```
npm run dev [args]
```
The [args] placeholder can be replaced with an English phrase to be translated to Braille, or Braille symbols to be translated to English. Ensure that the Braille symbols are represented correctly using the 'O' and '.' characters.

### Testing
In order to validate the accuracy and integrity of the application, a test has been included. It can be run using:

```
npm run test
```

