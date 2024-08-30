const { exec } = require("child_process");

describe("translator.js script", () => {
  // it("should correctly translate 'Hello world' to Braille", (done) => {
  //   exec("node translator.js Hello world", (error, stdout, stderr) => {
  //     expect(error).toBeNull();
  //     expect(stderr).toBe("");
  //     expect(stdout.trim()).toBe(".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..");
  //     done();
  //   });
  // });
  // it("should correctly translate '42' to Braille", (done) => {
  //   exec("node translator.js 42", (error, stdout, stderr) => {
  //     expect(error).toBeNull();
  //     expect(stderr).toBe("");
  //     expect(stdout.trim()).toBe(".O.OOOOO.O..O.O...");
  //     done();
  //   });
  // });
  // it("should correctly translate 'Abc 123 xYz' to Braille", (done) => {
  //   exec("node translator.js Abc 123 xYz", (error, stdout, stderr) => {
  //     expect(error).toBeNull();
  //     expect(stderr).toBe("");
  //     expect(stdout.trim()).toBe(".....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO");
  //     done();
  //   });
  // });
  // it("should correctly translate Braille '.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..' to text 'Abc 123'", (done) => {
  //   exec("node translator.js .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..", (error, stdout, stderr) => {
  //     expect(error).toBeNull();
  //     expect(stderr).toBe("");
  //     expect(stdout.trim()).toBe("Abc 123");
  //     done();
  //   });
  // });
});
