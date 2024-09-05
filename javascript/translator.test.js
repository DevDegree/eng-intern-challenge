const { exec } = require("child_process");
const Translator = require("./translator");

// describe('translator.js script', () => {
//     it('should output correct answer to the console', (done) => {
//         exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
//             expect(error).toBeNull();
//             expect(stderr).toBe("");
//             expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO");
//             done();
//         });
//     });
// });

it("should convert braille to english and vice versa", () => {
  expect(
    Translator(".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
  ).toBe("Abc 123");

  expect(Translator("Abc 123 xYz")).toBe(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
  );

  expect(Translator(42)).toBe(".O.OOOOO.O..O.O...");
  expect(Translator("Hello world")).toBe(
    ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
  );

});
