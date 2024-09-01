const {translateBrailleToEnglish} = require('./translators/braille-to-english');
const {translateEnglishToBraille} = require('./translators/english-to-braille');

const isInputBraille = (args) => {
    const regexBrailleStart = /^O{0,5}.(.*)$/;
    return args.length <= 1 && args[0].length % 6 === 0 && regexBrailleStart.test(args[0]);
};

const args = process.argv.slice(2);

if (isInputBraille(args)) {
    const sentence = args[0];
    translateBrailleToEnglish(sentence);
}
else {
    translateEnglishToBraille(args);
}
