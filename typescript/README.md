# TypeScript Instructions

<div align="center">

  <h2 align="center">Braille to English and English to Braille Translator</h2>

  <p align="center">
    Shopify Eng Intern Challenge - 2024
  </p>
</div>

A terminal / command-line application that can translate Braille to English and vice versa.

The string to translate will be passed into the application as an argument at runtime. The application is smart enough to determine if the string given to it is either Braille or English and automatically convert it to the appropriate opposite.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Node 20.12.2
npm 10.5.0

### Installing

A step by step series of examples that tell you how to get a development env running

```
npm install
```

### Usage

Run the following command to run the application, make sure to pass in command line arguments

```
npm run dev [a phrase of Braille or English]

// Examples
npm run dev Hello world
npm run dev .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

You can also use this command instead of npm

```
node-ts translator.ts [a phrase of Braille or English]
```

## Running tests

Located in the test file at `typescript/translator.test.ts`

```
npm run test
```

## Built With

[![](https://img.shields.io/badge/Node.js-000000?style=for-the-badge&logo=node.js&logoColor=white)]()
[![](https://img.shields.io/badge/Typescript-000000?style=for-the-badge&logo=typescript&logoColor=white)]()
[![](https://img.shields.io/badge/Jest-000000?style=for-the-badge&logo=Jest&logoColor=white)]()

## Contributing

If you see an issue or would like to contribute, please do & open a pull request or ticket for/with new features or fixes.

## Authors

- **Justin Zhang** - _Initial work_ - [JustinZhang17](https://github.com/JustinZhang17)

## Restrictions

- This program requires a sequence of numbers to end with a space character otherwise, it will not recognize its following english alphabet characters
- No special characters were considered as it was not defined in the technical program specifications
- The english alphabet refers to the 26 latin characters from A to Z (upper or lower case) and the program doesn't check if a string of latin characters is a valid english word.

