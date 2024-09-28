class Helper {
  constructor(alp, num) {
    this.alphabets = alp;
    this.numbers = num;
  }

  convert(data) {
    let tempData = data;

    if (tempData.replace(/[.O]/g, "").length == 0) {
      //   if after removing  "." and "O" we are left with nothing means we have Braille
      return this.convertBrailleToAlphabets(data);
    } else {
      //we have alpha numberic string
      return this.convertAlphaToBraille(data);
    }
  }

  //take in string and convert it to Braille
  convertAlphaToBraille(data) {
    let result = "";
    let num = false;

    for (let i = 0; i < data.length; i++) {
      if (data.charAt(i) >= "A" && data.charAt(i) <= "Z") {
        result += this.numbers.get("C");
        result += this.alphabets.get(data.charAt(i).toLowerCase());
      } else if (data.charAt(i) >= "a" && data.charAt(i) <= "z") {
        result += this.alphabets.get(data.charAt(i));
      } else if (data.charAt(i) == " ") {
        num = false;
        result += this.numbers.get(data.charAt(i));
      } else if (data.charAt(i) >= 0 && data.charAt(i) <= 9) {
        if (!num) {
          num = true;
          result += this.numbers.get("N");
        }

        result += this.numbers.get(data.charAt(i));
      }
    }
    return result;
  }

  //take in Braille and convert it to String
  convertBrailleToAlphabets(data) {
    let tempData = "";
    let result = "";
    let caps = false;
    let num = false;

    data = data + " ";

    for (let i = 0; i < data.length; i++) {
      if (i % 6 === 0 && i != 0) {
        if (num) {
          if (this.numbers.get(tempData) == " ") {
            num = false;
            result += " ";
          } else {
            result += this.numbers.get(tempData);
          }
        } else {
          if (this.alphabets.get(tempData) == " ") {
            result += " ";
            caps = false;
            num = false;
          } else if (this.alphabets.get(tempData) == "C") {
            caps = true;
          } else if (this.alphabets.get(tempData) == "N") {
            num = true;
            caps = false;
          } else {
            if (caps) {
              result += this.alphabets.get(tempData).toUpperCase();
              caps = false;
            } else {
              result += this.alphabets.get(tempData);
            }
          }
        }
        tempData = data.charAt(i);
      } else {
        tempData += data.charAt(i);
      }
    }
    return result;
  }
}

module.exports = Helper;
