const query = process.argv.slice(2).join(" ").trim().split("");

const dictionaryEnglish = {};
const dictionaryBraille = {};

const braille = ["O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "O...O.", "O.O.O.", "OO..O.", "OO.OO.", "O..OO.", "OOO.O.", "OOOOO.", "O.OOO.", ".OO.O.", ".OOOO.", "O...OO", "O.O.OO", ".OOO.O", "OO..OO", "OO.OOO", "O..OOO", "O.....", "O.O...", "OO....", "OO.O..", "O..O..", "OOO...", "OOOO..", "O.OO..", ".OO...", ".OOO..", "......"];

[..."abcdefghijklmnopqrstuvwxyz1234567890 "].forEach((l, i) => {
    dictionaryEnglish[l] = braille[i];
    dictionaryBraille[braille[i]] ? dictionaryBraille[braille[i]] += l : dictionaryBraille[braille[i]] = l;
});

const options = {
    capital: ".....O",
    number: ".O.OOO",
};

const determinator = query.every(l => l === "." || l === "O") ? "Braille" : "English"

if (determinator === "English") {

    const englishToBraille = query.map((l, i) => {

        if (l === " ") {
            return "......"
        }

        if ( l === l.toUpperCase() && (i === 0 || query[i - 1] !== query[i - 1].toUpperCase()) ) {
            return options.capital + dictionaryEnglish[l.toLowerCase()]
        }

        if (!isNaN(+l) && (isNaN(+query[i - 1]) || query[i - 1] === " " )) {
            return options.number + dictionaryEnglish[l]
        }

        return dictionaryEnglish[l.toLowerCase()]

    }).join("")

    console.log(englishToBraille)

} else {

    const brailleSegments = query.reduce((cT, cV) => {
        cT[cT.length - 1].length === 6 ? cT.push(cV) : cT[cT.length - 1] += cV
        return cT
    }, [""])

    let capital = false
    let number = false

    const brailleToEnglish = brailleSegments.map(segment => {

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

    console.log(brailleToEnglish)

}