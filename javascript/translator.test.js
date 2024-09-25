const { exec } = require('child_process');
// const { execSync } = require('child_process');

// function textToBraille(text) {
//   try {
//     const stdout = execSync(`node translator.js "${text}"`, { encoding: 'utf-8' });
//     return stdout.trim();
//   } catch (error) {
//     throw new Error(`Error in textToBraille: ${error.message}`);
//   }
// }

// function brailleToText(braille) {
//   try {
//     const stdout = execSync(`node translator.js "${braille}"`, { encoding: 'utf-8' });
//     return stdout.trim();
//   } catch (error) {
//     throw new Error(`Error in brailleToText: ${error.message}`);
//   }
// }

// describe('translator.js script', () => {
//   const testCases = [
//     "hello world",
//     "3 > 2",
//     "5.2314",
//     "abc123xyz",
//     "hello 123 world",
//     "1.23 < 4.56",
//     "test? yes!",
//     "a1b2c3",
//     "3.14 > pi",
//     "(start) 123 (end)",
//     "1st 2nd 3rd",
//     "a.b.c. 1.2.3",
//     "100 > 90",
//     "x-ray / z-axis",
//     "q1: 1,234.56",
//     "user: tag 123",
//     "(a+b) / c = 123",
//     "10:30 - 14:4566666",
//     "isbn: 978-0-123456-47-2",
//     "a1b2c3 > x1y2z3"
//   ];

//   testCases.forEach((testInput) => {
//     it(`should correctly translate "${testInput}" to Braille and back`, () => {
//       const braille = textToBraille(testInput);
//       const testOutput = brailleToText(braille);

//       expect(testOutput.toLowerCase()).toBe(testInput.toLowerCase());
//     });
//   });
// });

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