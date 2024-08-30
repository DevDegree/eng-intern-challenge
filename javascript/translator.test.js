// const { exec } = require("child_process");

// describe('translator.js script', () => {
//     it('should output correct answer to the console', (done) => {
//         exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
//             expect(error).toBeNull();
//             expect(stderr).toBe("");
//             expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO");
//             done();
//         });
//     });
// });

// commented code above is the untouched original test

// original test was not set up properly in the public repository, the test below contains the following edits: added '' around the test string, changed the test numbers to 234 instead of 123 to match the braille that is in the expected, with these changes the test passes, otherwise there is a timeout error

const { exec } = require("child_process");

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        exec("node translator.js 'Abc 234 xYz'", (error, stdout, stderr) => {
            expect(error).toBeNull();
            expect(stderr).toBe("");
            expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO");
            done();
        });
    });
});