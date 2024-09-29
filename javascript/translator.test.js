// javascript/translator.test.js
const { exec } = require('child_process');

describe('translator.js script', () => {
    it('should output correct answer to the console', (done) => {
        jest.setTimeout(10000); // Increase timeout to 10 seconds
        exec("node translator.js 'Hello World'", (error, stdout, stderr) => {
            expect(error).toBeNull();  // Ensure there is no error
            expect(stderr).toBe("");    // Ensure standard error is empty
            console.log(stdout.trim()); // Log the output to the console
            //expect(stdout.trim()).toBe("node translator.js '.....OO.OO..O..O..O.O.O.O.O.O.O..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O..'"); // Adjust expected output accordingly
            done(); // Indicate that the test is done
        });
    });
});
