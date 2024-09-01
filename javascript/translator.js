const query = process.argv.slice(2).join(" ").split("");

const dictionary = {};

const braille = ["0.....", "0.0...", "00....", "00.0..", "0..0..", "000...", "0000..", "0.00..", ".00...", ".000..", "0...0.", "0.0.0.", "00..0.", "00.00.", "0..00.", "000.0.", "00000.", "0.000.", ".00.0.", ".0000.", "0...00", "0.0.00", ".000.0", "00..00", "00.000", "0..000", "0.....", "0.0...", "00....", "00.0..", "0..0..", "000...", "0000..", "0.00..", ".00...", ".000..", "..00.0", "..0...", "..0.00", "..000.", "..00..", "..0.0.", "....00", ".0..0.", ".00..0", "0..00.", "0.0..0", ".0.00.", "......"];

const english = [..."abcdefghijklmnopqrstuvwxyz1234567890.,?!:;-/<>() "].forEach((l, i) => dictionary[l] = braille[i]);

const options = {
    capital: ".....0",
    number: ".0.000",
    decimal: ".0...0"
};

const determinator = query.every(l => l === "." || l === "0") ? "Braille" : "English"

if (determinator === "English") {

    return query.map((l, i) => {

        if ((i === 0 && l === l.toUpperCase()) || (l === l.toUpperCase() && query[i - 1] !== query[i - 1].toUpperCase() && i > 0)) {
            return options.capital + dictionary[l]
        }

        if (typeof(+l) === "number" && !isNaN(+l) && typeof(+query[i - 1]) !== "number") {
            return options.number + dictionary[l]
        }

        if (l === "." && typeof(+query[i - 1]) === "number" && !isNaN(+query[i - 1]) && typeof(+query[i + 1]) === "number" && !isNaN(+query[i + 1])) {
            return options.decimal
        }

        return dictionary[l.toLowerCase()]

    }).join("")

} else {

}