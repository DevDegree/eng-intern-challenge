import { Strings, brailleMap } from './constants';
import MenuPromptService from './services/menuPromptService';

class Translator {
    private readonly menuPromptService: MenuPromptService;

    constructor() {
        this.menuPromptService = new MenuPromptService();
    }

    /**
     * Main run method for the Translator CLI
     * Handles interactive mode or direct translation based on input
     */
    public async run(words: string[]): Promise<void> {
        if (words.length > 0) {
            await this.translateText(words);
        } else {
            await this.runInteractiveMode();
        }
    }

    /**
     * Runs the interactive mode with menu prompts
     */
    private async runInteractiveMode(): Promise<void> {
        let isRunning = true;
        while (isRunning) {
            const action = await this.menuPromptService.promptMainMenu();
            isRunning = await this.handleMainMenuAction(action);
        }
        console.log('👋 Exiting...');
    }

    /**
     * Handles the main menu action
     * @param action - The selected action from the main menu
     * @returns boolean indicating whether to continue running
     */
    private async handleMainMenuAction(action: string): Promise<boolean> {
        switch (action) {
            case Strings.ACTIONS.TRANSLATE:
                await this.handleTranslateAction();
                console.log('\n');
                return true;
            case Strings.ACTIONS.EXIT:
                return false;
            default:
                console.log(Strings.MESSAGES.INVALID_ACTION);
                return true;
        }
    }

    /**
     * Translates the given text and outputs the result
     */
    private async translateText(words: string[]): Promise<void> {
        const text = words.join(' ');
        if (this.isBraille(text)) {
            const translatedText = this.translateBrailleToEnglish(text);
            console.log(translatedText);
        } else {
            const translatedText = this.translateEnglishToBraille(text);
            console.log(translatedText);
        }
    }

    /**
     * Handles the translate action
     * Prompts for text and translates it
     */
    private async handleTranslateAction(): Promise<void> {
        const text = await this.menuPromptService.promptForText();
        if (this.isBraille(text)) {
            const translatedText = this.translateBrailleToEnglish(text);
            console.log(translatedText);
        } else {
            const translatedText = this.translateEnglishToBraille(text);
            console.log(translatedText);
        }
    }

    // Function to determine if input is Braille or English
    private isBraille(input: string): boolean {
        return /^[O.]+$/.test(input.replace(/\s/g, ''));
    }

    // Function to convert Braille to English
    private translateBrailleToEnglish(input: string): string {
        const brailleSymbols = input.match(/.{6}/g);
        if (!brailleSymbols) {
            return '';
        }
        let translation = '';
        let isCapital = false;
        let isNumber = false;

        brailleSymbols.forEach(symbol => {
            if (symbol === ".....O") {
                isCapital = true;
            } else if (symbol === ".O.OOO") {
                isNumber = true;
            } else if (symbol in brailleMap.brailleToEnglishAlphabets) {
                if (isNumber) {
                    translation += brailleMap.brailleToEnglishDigits[symbol] || '';
                } else {
                    let letter = brailleMap.brailleToEnglishAlphabets[symbol];
                    if (isCapital && letter !== ' ') {
                        letter = letter.toUpperCase();
                        isCapital = false;
                    }
                    translation += letter;
                }
            } else if (symbol === "......") {
                translation += ' ';
                isNumber = false;
            }
        });
        return translation;
    }

    // Function to convert English to Braille
    private translateEnglishToBraille(input: string): string {
        let translation = '';
        let isNumber = false;
        let words = input.split(' ');

        for (let i = 0; i < words.length; i++) {
            let word = words[i];
            for (let char of word) {
                if (/[A-Z]/.test(char)) {
                    translation += brailleMap.englishAlphabetsToBraille['capital'];
                    translation += brailleMap.englishAlphabetsToBraille[char.toLowerCase()];
                } else if (/[a-z]/.test(char)) {
                    translation += brailleMap.englishAlphabetsToBraille[char];
                } else if (/\d/.test(char)) {
                    if (!isNumber) {
                        translation += brailleMap.englishAlphabetsToBraille['number'];
                        isNumber = true;
                    }
                    translation += brailleMap.englishDigitsToBraille[char];
                } else {
                    if (isNumber && /\D/.test(char)) {
                        isNumber = false;
                    }
                    translation += brailleMap.englishAlphabetsToBraille[char.toLowerCase()] || '';
                }
            }
            // Add six periods (Braille space) between words, except for the last word
            if (i < words.length - 1) {
                translation += '......';
            }
        }
        return translation;
    }
}

export default Translator;