const query = process.argv.slice(2).join(" ").trim().split("");

const dictionaryEnglish = {};
const dictionaryBraille = {};

const english = [..."abcdefghijklmnopqrstuvwxyz1234567890 "];
const braille = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "......"];

const options = {
    capital: ".....O",
    number: ".O.OOO",
};

english.forEach((l, i) => {
    dictionaryEnglish[l] = braille[i];
    dictionaryBraille[braille[i]] ? dictionaryBraille[braille[i]] += l : dictionaryBraille[braille[i]] = l;
});

const englishToBraille = () => {

    const brailleString = query.map((l, i) => {

        if (!english.includes(l.toLowerCase())) {
            throw new Error(`Invalid character included: ${l}`)
        }

        if (l === " ") {
            return "......"
        }

        if (!isNaN(+l) && (isNaN(+query[i - 1]) || query[i - 1] === " " )) {
            return options.number + dictionaryEnglish[l]
        }

        if ( l === l.toUpperCase() && (i === 0 || query[i - 1] !== query[i - 1].toUpperCase()) ) {
            return options.capital + dictionaryEnglish[l.toLowerCase()]
        }

        return dictionaryEnglish[l.toLowerCase()]

    }).join("")

    console.log(brailleString)

}

const brailleToEnglish = () => {

    const brailleSegments = query.reduce((cT, cV) => {
        cT[cT.length - 1].length === 6 ? cT.push(cV) : cT[cT.length - 1] += cV
        return cT
    }, [""])

    let capital = false
    let number = false

    const englishString = brailleSegments.map(segment => {

        if (!braille.includes(segment) && segment !== options.capital && segment !== options.number) {
            throw new Error(`Invalid braille character included. Please check input.`)
        }

        if (segment === options.capital || capital) { 
            if (capital) {
                capital = false
                return dictionaryBraille[segment][0].toUpperCase()
            } else {
                capital = true
                return "SKIP" 
            }
        }

        if (segment === options.number || number) {
            if (number && segment === "......") {
                number = false
                return " "
            } else if (number) {
                return dictionaryBraille[segment][1]
            } else {
                number = true
                return "SKIP"
            }
        }

        return dictionaryBraille[segment][0]

    }).filter(char => char !== "SKIP").join("")

    console.log(englishString)

}

query.every(l => l === "." || l === "O") ? brailleToEnglish() : englishToBraille();