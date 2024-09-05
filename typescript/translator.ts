type brailleChar = '.' | 'O';
type brailleTable = Record<string,
    `${brailleChar}${brailleChar}${brailleChar}${brailleChar}${brailleChar}${brailleChar}`>;

try {
    if (process.argv.length < 3) {
        process.exit(-1);
    }

    const LOW_CASE_FOLLOWS = "LOW_CASE_FOLLOWS";
    const UPPER_CASE_FOLLOWS = "UPPER_CASE_FOLLOWS";
    const NUMBER_FOLLOWS = "NUMBER_FOLLOWS";

    const BRAILLE: brailleTable = {
        [UPPER_CASE_FOLLOWS]: ".....O",
        [NUMBER_FOLLOWS]: ".O.OOO",
        a: "O.....",
        b: "O.O...",
        c: "OO....",
        d: "OO.O..",
        e: "O..O..",
        f: "OOO...",
        g: "OOOO..",
        h: "O.OO..",
        i: ".OO...",
        j: ".OOO..",
        k: "O...O.",
        l: "O.O.O.",
        m: "OO..O.",
        n: "OO.OO.",
        o: "O..OO.",
        p: "OOO.O.",
        q: "OOOOO.",
        r: "O.OOO.",
        s: ".OO.O.",
        t: ".OOOO.",
        u: "O...OO",
        v: "O.O.OO",
        w: ".OOO.O",
        x: "OO..OO",
        y: "OO.OOO",
        z: "O..OOO",
        1: "O.....",
        2: "O.O...",
        3: "OO....",
        4: "OO.O..",
        5: "O..O..",
        6: "OOO...",
        7: "OOOO..",
        8: "O.OO..",
        9: ".OO...",
        0: ".OOO..",
        " ": "......",
    };

    const args = process.argv.slice(2);
    const regExpBraille = /[.O]{6}/g;
    const regExpEng = /.{1}/g;

    function isReverse(wrords: Array<string>) {
        return (
            wrords.length === 1 && wrords[0].length % 6 === 0 && !!wrords[0].match(regExpBraille)
        );
    }

    function getTranslationTable(isRev: boolean) {
        if (!isRev) {
            return BRAILLE;
        }

        return Object.entries(BRAILLE)
            .reverse()
            .reduce(
                (acc, [engChar, braille]) => {
                    const brailleToEnglish = acc[braille]
                        ? {
                            NUMBER_FOLLOWS: {
                                ...acc.NUMBER_FOLLOWS,
                                [braille]: engChar,
                            },
                        }
                        : {[braille]: engChar};

                    return {
                        ...acc,
                        ...brailleToEnglish,
                    };
                },
                {NUMBER_FOLLOWS: {}} as Record<string, any>
            );
    }

    function translate(words: Array<string>) {
        const isRev = isReverse(words);
        const table = getTranslationTable(isRev);
        const regExp = isRev ? regExpBraille : regExpEng;
        const space = table[isRev ? "......" : " "];

        const matrixRes = words.reduce(
            (acc, word) => {
                let state = acc.state;
                const chars = word
                    // split word on chars
                    .match(regExp)
                    .map((char) => {
                        if (isRev) {
                            if (state === NUMBER_FOLLOWS) {
                                if (table[NUMBER_FOLLOWS][char]) {
                                    return table[NUMBER_FOLLOWS][char];
                                } else if (table[char] === ";") {
                                    state = LOW_CASE_FOLLOWS;
                                    return null;
                                }
                                state = LOW_CASE_FOLLOWS;
                            }
                            if (table[char] === UPPER_CASE_FOLLOWS) {
                                state = UPPER_CASE_FOLLOWS;
                                return null;
                            }
                            if (table[char] === NUMBER_FOLLOWS) {
                                state = NUMBER_FOLLOWS;
                                return null;
                            }
                            if (state === UPPER_CASE_FOLLOWS) {
                                state = LOW_CASE_FOLLOWS;
                                return table[char].toUpperCase();
                            }
                            return table[char];
                        }
                        if (char.match(/\d/)) {
                            if (state === NUMBER_FOLLOWS) {
                                return table[char];
                            }
                            state = NUMBER_FOLLOWS;
                            return `${table[NUMBER_FOLLOWS]}${table[`${char}`]}`;
                        }
                        if (char === char.toLowerCase()) {
                            if (state === NUMBER_FOLLOWS) {
                                state = LOW_CASE_FOLLOWS;
                                return `${table[char]}`;
                            }
                            state = LOW_CASE_FOLLOWS;
                            return table[char];
                        }
                        if (char === char.toUpperCase()) {
                            state = UPPER_CASE_FOLLOWS;
                            return `${table[UPPER_CASE_FOLLOWS]}${table[char.toLowerCase()]}`;
                        }
                    })
                    .filter((v) => v !== null);

                return {
                    state,
                    result: [...acc.result, chars],
                };
            },
            {
                state: LOW_CASE_FOLLOWS,
                result: [],
            }
        );

        return matrixRes.result.map((char) => char.join("")).join(space);
    }

    const result = translate(args);
    console.log(result);
    //console.log("forward translate is:", result);
    //console.log("and translate it back is:", `***${translate([result])}***`);
} catch (e) {
    process.exit(-2);
}
