const brailleSpecials = {
    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
};

const reverseBrailleSpecials = {
    '......': ' ',
    '.....O': 'capital',
    '.O.OOO': 'number'
};

module.exports = { brailleSpecials, reverseBrailleSpecials }