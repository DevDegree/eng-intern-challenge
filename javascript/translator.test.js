const { exec } = require("child_process");

// English to braille Tests
describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js Hello world", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
            done();
        });
    });
});

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js 42", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O..O.O...");
            done();
        });
    });
});

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO");
            done();
        });
    });
});
