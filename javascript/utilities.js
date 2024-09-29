const isLetter = (item) => {
    return /^[A-Za-z]$/.test(item);
}

const isUpper = (item) => {
    return /^[A-Z]$/.test(item);
}

const isNumber = (item) => {
    return /^\d$/.test(item);
}

module.exports = {
    isLetter,
    isUpper,
    isNumber
}