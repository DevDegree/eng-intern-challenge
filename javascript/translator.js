#!/usr/bin/env node

class BrailleTranslator {
    constructor() {
        this.brailleMap = {
            'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
            'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
            'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
            'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
            'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 'z': 'O..OOO',
            '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
            '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..',
            ' ': '......', 'cap': '.....O', 'num': '.O.OOO'
        }
        this.textMap = Object.fromEntries(Object.entries(this.brailleMap).map(([k, v]) => [v, k]))
    }

    detectInputType(input) {
        return /^[O.]+$/.test(input) && input.length % 6 === 0 ? 'braille' : 'text'
    }

    translateToBraille(text) {
        let braille = '', isNumber = false
        for (let char of text) {
            if (/[A-Z]/.test(char)) braille += this.brailleMap['cap'], char = char.toLowerCase()
            if (/\d/.test(char) && !isNumber) braille += this.brailleMap['num'], isNumber = true
            if (/\s/.test(char)) isNumber = false
            braille += this.brailleMap[char] || ''
        }
        return braille
    }

    translateToText(braille) {
        let text = '', isCapital = false, isNumber = false
        for (let i = 0; i < braille.length; i += 6) {
            const brailleChar = braille.slice(i, i + 6)
            if (brailleChar === this.brailleMap['cap']) isCapital = true
            else if (brailleChar === this.brailleMap['num']) isNumber = true
            else {
                const char = this.textMap[brailleChar] || ''
                text += isNumber && /\d/.test(char) ? char : isCapital ? char.toUpperCase() : char
                isCapital = isNumber = false
            }
        }
        return text
    }

    translate(input) {
        return this.detectInputType(input) === 'text' ? this.translateToBraille(input) : this.translateToText(input)
    }
}

if (process.argv.length > 2) {
    const input = process.argv.slice(2).join(' ')
    console.log(new BrailleTranslator().translate(input))
} else {
    console.log("Please provide text or Braille input.")
}
