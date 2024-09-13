export function detectInputType(input) {
    return /^[O.\s]+$/.test(input) ? "braille" : "english";
}


export function splitIntoBrailleCells(braille) {
    return braille.match(/.{1,6}/g) || [];
}

export function isDigit(character) {
    return character >= "0" && character <= "9";
}

export function isUppercase(character) {
    return character.toUpperCase() === character && character.toLowerCase() !== character;
}

export function findCharacterInMap(map, value) {
    return Object.keys(map).find(key => map[key] === value);
}