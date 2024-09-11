const { exec } = require("child_process");

describe('translator.js script', () => {
    it('should output correct answer from english to braille to the console', (done) => {
        exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO");
            done();
        });
    });
    it('should output correct answer from english to braille to the console', (done) => {
        exec("node translator.js Hello How aRe 328 toDay", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.OO..O..O..O.O.O.O.O.O.O..OO............OO.OO..O..OO..OOO.O......O..........OO.OOO.O..O.........O.OOOOO....O.O...O.OO.........OOOO.O..OO......OOO.O..O.....OO.OOO");
            done();
        });
    });
    it('should output correct answer from braille to english to the console', (done) => {
        exec("node translator.js .....OO.OO..O..O..O.O.O.O.O.O.O..OO............OO.OO..O..OO..OOO.O......O..........OO.OOO.O..O.........O.OOOOO....O.O...O.OO.........OOOO.O..OO......OOO.O..O.....OO.OOO", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("Hello How aRe 328 toDay");
            done();
        });
    });
    it('should output correct answer from braille to english to the console', (done) => {
        exec("node translator.js .OOOO.O.OO.......O.OO....OO.O........OO....OO.O............OO...........OO....O..OO.OO..O.OOO.O.O.O.O.O..O.......OOO..OO.......OOO.O.....OO..OO.O.OOO......OOO.O.........O.OOOOO....O.OO...OO....OOO..", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("thIs is A compleX wOrD 3890");
            done();
        });
    });
});
