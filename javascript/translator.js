const { engToBr, brToEng, brToNum } = require('./dictionaries')

// Access command line arguments and convert to string
const args = process.argv.slice(2)
const input = args.join(' ')

const ENGLISH = 1

// Determine type of the input
const determineType = () => {
    const firstSixLetters = input.slice(0, 6)
    if (firstSixLetters in brToEng || firstSixLetters in brToNum) return 0
    return 1
}

const type = determineType()

if (type === ENGLISH) {
    const isCapital = (char) => /^[A-Z]$/.test(char)
    const isNumber = (char) => /^[0-9]$/.test(char)

    for (let i = 0; i < input.length; i++) {
        if (isNumber(input[i])) {
            process.stdout.write(engToBr['num'])
            // Process the numbers until a space or end of input
            while (i < input.length && input[i] !== ' ') {
                process.stdout.write(engToBr[input[i]])
                i++
            }
            i--
        } else {
            if (isCapital(input[i])) {
                process.stdout.write(engToBr['cap'])
            }
            process.stdout.write(engToBr[input[i].toLowerCase()])
        }
    }
} else {
    let curr = 'letter'
    for (let i = 0; i < input.length; i += 6) {
        const chunk = input.slice(i, i + 6)

        // check number symbol
        if (chunk === '.O.OOO') {
            curr = 'number'
            continue
        }

        // check if space
        if (chunk === '......') {
            curr === 'letter'
        }

        // check if capital
        if (curr === 'number') {
            process.stdout.write(brToNum[chunk])
        } else {
            if (chunk === '.....O') {
                i += 6 // skip to next
                const nextChunk = input.slice(i, i + 6)
                process.stdout.write(brToEng[nextChunk].toUpperCase())
            } else {
                process.stdout.write(brToEng[chunk])
            }
        }
    }
}

// .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
// .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
