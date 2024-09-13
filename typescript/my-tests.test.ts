import isBraille from "./isBraille";

describe("test isBraille", () => {
  it("false if less than 6 characters", async () => {
    let result = isBraille("0...");
    expect(result).toBeFalsy();
  });
  it("false if more than 6 characters", async () => {
    let result = isBraille(".......");
    expect(result).toBeFalsy();
  });
  it("false if it contains a letter other than o or .", async () => {
    let result = isBraille("...oa.");
    expect(result).toBeFalsy();
  });
  it("true if valid braille", async () => {
    let result = isBraille("...o..");
    expect(result).toBeTruthy();
  });
});
