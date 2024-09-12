//PSEUDOCODE

//create English to braille object*
//create braille to English object*
//*consider making seperate objects for alphabet characters and letters for better readability and reuseability. 
//**note that the braille alphabet for the letter O and the > symbol are the same. find a solution after your basic code works./ 

//function to detect language (English or braille), then convert to opposite language with one of the correspoding two functions below.
    //maybe detect if language is only in O and . using a regex.

//function to tranlate English to braille
    //use split() method to split the string into individual characters.
    //use map() method to map over all characters.
        //if alphabet letter is capitalized, add braille indicator for capital follows before the corresponding braille sympbol. 
            //ensure only the character that follows the braille indicator for capital follows is capitalized. maybe use boolean here. 
        //if character is a number, add braille indicator for number follows before the corresponding braille symbol.
            //ensure all characters that follow the braille indicator for number follows are numbers until the use hits space bar. maybe use boolean here. 
            //if decimal is used, add braille indicator for decimal follows before the corresponding braille symbol, else print braille symbol for period. 
        //return all characters
    //use join() method to concatenate all characters into a string 
    

//function to translate braille to English
    //since braille segements follow a six dot pattern, create a regex for 6 characters
    //use regex and match() method to split the braille into 6-chacter segments
    //use map() method to map over all the segments and follow logic in function above
    //use join() method to concatenate all characters into a string