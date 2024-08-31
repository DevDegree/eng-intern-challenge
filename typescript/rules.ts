export type Rule = {
    english: string;
    braille: string;
}

export const CAPITAL_FOLLOWS = "CAPITAL";
export const DECIMAL_FOLLOWS = "DECIMAL";
export const NUMBER_FOLLOWS = "NUMBER";
export const SPACE = " ";

export const rules: Rule[] = [
    {
        english: "a",
        braille: "O....."
    },
    {
        english: "b",
        braille: "O.O...",
    },
    {
        english: "c",
        braille: "OO...."
    },
    {
        english: "d",
        braille: "OO.O.."
    },
    {
        english: "e",
        braille: "O..O.."
    },
    {
        english: "f",
        braille: "OOO..."
    },
    {
        english: "g",
        braille: "OOOO.."
    },
    {
        english: "h",
        braille: "O.OO.."
    },

    {
        english: "i",
        braille: ".OO..."
    },
    {
        english: "j",
        braille: ".OOO.."
    },
    {
        english: "k",
        braille: "O...O."
    },
    {
        english: "l",
        braille: "O.O.O."
    },  
    {
        english: "m",
        braille: "OO..O."
    },
    {
        english: "n",
        braille: "OO.OO."
    },
    {
        english: "o",
        braille: "O..OO."
    },
    {
        english: "p",
        braille: "OOO.O."
    },
    {
        english: "q",
        braille: "OOOOO."
    },
    {
        english: "r",
        braille: "O.OOO."
    },
    {
        english: "s",
        braille: ".OO.O."
    },
    {
        english: "t",
        braille: ".OOOO."
    },
    {
        english: "u",
        braille: "O...OO"
    },
    {
        english: "v",
        braille: "O.O.OO"
    },
    {
        english: "w",
        braille: ".OOO.O"
    },
    {
        english: "x",
        braille: "OO..OO"
    },
    {
        english: "y",
        braille: "OO.OOO"
    },
    {
        english: "z",
        braille: "O..OOO"
    },
    {
        english: SPACE,
        braille: "......"
    },
    {
        english: CAPITAL_FOLLOWS,
        braille: ".....O"
    },
    {
        english: DECIMAL_FOLLOWS,
        braille: ".O...O"
    },
    {
        english: NUMBER_FOLLOWS,
        braille: ".O.OOO"
    }
];