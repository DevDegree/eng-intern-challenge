import * as process from 'process';
import { Translator } from './translator-class';
let words: string[] = [];
for (let i = 2; i < process.argv.length; i++) {
    words.push(process.argv[i]);
}

const translator = new Translator();
console.log(translator.translate(words));

