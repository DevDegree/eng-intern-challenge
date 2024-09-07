/*
Options:
Queue
For Loop

Init two hashmaps for English and Braille
init output
Check for elements outside of . and O
    - if true, English else Braille
English:
Iterate over each element in the string
For each element, search hash for character and append to output

Braille:
Iterate over 6 elements
Search hash for corresponding character
*/
function brailleTranslator(word) {
    var output = "";
    for (var i = 0; i < 3; i++) {
        var regexp = /\b\w*[.O]\w*\b/;
        if (regexp.test(word)) {
            console.log(true);
        }
    }
    console.log("Working");
}
var word = "abc123";
brailleTranslator(word);
console.log("working");
