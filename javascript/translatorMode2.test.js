const { exec } = require("child_process");

describe("translator.js script", () => {
  it("should output correct answer to the console", (done) => {
    exec("node translator.js -mode2 Abc 123 xYz", (error, stdout, stderr) => {
      expect(error).toBeNull();
      expect(stderr).toBe("");
      expect(stdout.trim()).toBe(
        ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
      );
      done();
    });
  });
});

describe("translator.js script 1", () => {
  it("should output correct answer to the console", (done) => {
    exec("node translator.js -mode2 Hello world", (error, stdout, stderr) => {
      expect(error).toBeNull();
      expect(stderr).toBe("");
      expect(stdout.trim()).toBe(
        ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
      );
      done();
    });
  });
});

describe("translator.js script 2", () => {
  it("should output correct answer to the console", (done) => {
    exec("node translator.js -mode2 42", (error, stdout, stderr) => {
      expect(error).toBeNull();
      expect(stderr).toBe("");
      expect(stdout.trim()).toBe(".O.OOOOO.O..O.O...");
      done();
    });
  });
});
describe("translator.js script 3", () => {
  it("should output correct answer to the console", (done) => {
    exec(
      "node translator.js -mode2 .....OO.....O.O...OO...........O.OOOO.O...OO....OO.O..",
      (error, stdout, stderr) => {
        expect(error).toBeNull();
        expect(stderr).toBe("");
        expect(stdout.trim()).toBe("Abc 234");
        done();
      }
    );
  });
});
