const { exec } = require("child_process");

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO");
            done();
        });
    });

    it('should output correct answer to the console', (done) => {
        exec("node translator.js Hello world", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
            done();
        });
    });

    it('should output correct answer to the console', (done) => {
        exec("node translator.js 42", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".O.OOOOO.O..O.O...");
            done();
        });
    });

    it('should output correct answer to the console', (done) => {
        exec("node translator.js .....OO.....O.O...OO...........O.OOOO.....O.O...OO....", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("Abc 123");
            done();
        });
    });

    it('should output correct answer to the console', (done) => {
        exec("node translator.js .....OO.....O.O...OO........OO.O.OOOO.....O.O...OO....", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("Abc-123");
            done();
        });
    });

    it('should output correct answer to the console', (done) => {
        exec("node translator.js .O.OOOOO.....O...OOO.O..", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe("3.4");
            done();
        });
    });
});
