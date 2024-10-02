export class TranslationError extends Error {
    constructor(message, code) {
        super(message);
        this.name = 'TranslationError';
        this.code = code;
    }
}