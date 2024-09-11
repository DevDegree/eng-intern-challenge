# Braille Translator

A TypeScript-based CLI application for translating between English and Braille.

## Installation

```
npm install
```

## Build

```
npm run build
```

## Usage

### Direct Translation

Translate English to Braille or Braille to English directly:

```
node build/translator.js <text>
```

Examples:
```
node build/translator.js Hello world
node build/translator.js 42
node build/translator.js .O.OOOOO.O..O.O...
```

### Interactive Mode

Run the application in interactive mode:

```
node build/translator.js
```

This opens a menu-driven interface for continuous translations until you choose to exit.

## Features

- Bidirectional translation between English and Braille
- Support for uppercase letters, numbers, and spaces
- Interactive CLI with user-friendly prompts

## Testing

Run the test suite:

```
npm test
```