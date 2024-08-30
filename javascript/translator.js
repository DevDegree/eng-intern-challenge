/* 
Create hashmaps:
  Braille to English keys:
    - letters + spaces + capital follows + number follows
    - numbers + spaces
  English to Braille keys:
    - letters + numbers + spaces (don't forget to add follows symbols) 

Main function to export:
  Determine if string argument is Braille or English
    If length of string < 6, it is English
    Else, search for string in Braille to English hashmap(s)
      If string in hashmaps, string is in Braille
        Pass string to appropriate translator function
      Else, string is in English
        Pass string to appropriate translator function

Braille to English translator function:
  Create isCapital and isNumber variables
  Create output variable
  Iterate over string, taking in 6 characters at a time
    Translate string.substr(i, i + 5) from Braille to English using hashmap
    Add translated character to output
    Continue iterating until end of string is reached
  Output translated string

English to Braille translator function:
  Create capitalSymbol and numberSymbol variables
  Create numberMode variable
  Create output variable
  Iterate over string, 1 character at a time
    If string[i] is a capital letter
      Add isCapital symbol to output
      Take lowercase string[i] and add its respective Braille symbol to output
    Else if string[i] is a number
      If numberMode === false
        Set numberMode = true
        Add isNumber symbol to output
      Add respective Braille symbol for string[i] to output
    Else (string[i] === ' ')
      Set numberMode = false
      Add Braille symbol for space to output
  Output translated string
*/
