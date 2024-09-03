/*
example run:
node translator.js Hello world
 */

import {brailleAlphabet as brailleAlphabet, 
    englishAlphabet as englishAlphabet, 
    brailleNumbers as brailleNumbers, 
    englishNumbers as englishNumbers} from './utils/dictionary.js';

let msg = [];
let allText = "";

for (let i=2; i<process.argv.length; i++) {
    allText += process.argv[i];
    allText += " ";
}

for (let i=0; i<allText.length; i++) {
    msg.push(allText[i]);
}

msg.pop(); // remove final " "

let translatedMsg = "";
let msgIsEnglish = true;
let useNumbers = false;
let brailleChunks = [];

if (msg.includes(".")) {
    msgIsEnglish = false;
}

for (let i=0; i<msg.length; i++) {
    if (msgIsEnglish) {
        if (msg[i] === " ") {
            useNumbers = false;
        }

        if (msg[i] === msg[i].toUpperCase() && msg[i] != " " && !(msg[i] in brailleNumbers)) {
            translatedMsg += brailleAlphabet["capital"];
            translatedMsg += brailleAlphabet[msg[i].toLowerCase()];
        }

        else {
            if (msg[i] in brailleNumbers && !useNumbers) {
                useNumbers = true;
                translatedMsg += brailleAlphabet["number"];
                translatedMsg += brailleNumbers[msg[i]];
            }

            else if (msg[i] in brailleNumbers && useNumbers) {
                translatedMsg += brailleNumbers[msg[i]];
            }

            else {
                translatedMsg += brailleAlphabet[msg[i]];
            }
        }
    }
}

if (!msgIsEnglish) {
    msg = (process.argv[2]);

    for (let i=0; i<msg.length; i+=6) {
        brailleChunks.push(msg.substring(i,i+6));
    }

    for (let i=0; i<brailleChunks.length; i++) {
        if (brailleChunks[i] === ".....O") {
            translatedMsg += englishAlphabet[brailleChunks[i+1]].toUpperCase();
            i+=2;
        }

        if (brailleChunks[i] === ".O.OOO") {
            useNumbers = true;
            translatedMsg += englishNumbers[brailleChunks[i+1]];
            i+=2;
        }

        if (useNumbers) {
            translatedMsg += englishNumbers[brailleChunks[i]];
        }

        else {
            translatedMsg += englishAlphabet[brailleChunks[i]];
        }
    }
}

console.log(translatedMsg);