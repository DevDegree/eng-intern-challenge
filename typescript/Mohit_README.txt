For this challenge I decided to break up the problem into separate functions. One function would convert braille to English and the other does the opposite; the return of both functions is a converted string. To determine if the input arg was braille or English I made sure string length >= 6 and it only had O’s and .’s

In addition to this I created separate folders that would hold constants, language mapping and reusable functions that would be used by both translators for clarity. I created a hashmap to map alphabets, digits and punctuations to their braille equivalent and then reversed the hashmap. I understand that it may consume more memory but the tradeoff of O(1) access would be better if scaled.

In both functions I am passing in the given string and then converting them into an array, which is then passed into separate functions for the convertsion. For the brailled string, each entry would be made of 6 chars since that’s what a braille cell in the problem context was. The reason for using arrays was because they provide readability and flexible operations. 

One assumption, also based on research, was that anytime we have a decimal number of < or >, the number follows identifier was placed first followed by other digits or math related symbols (< and >)

brailleToEngTranslator.ts:

Began by importing needed functions, constants and maps
Used a for loop to iterate over each element and initially check to see if it was capital or number follows and if set the appropriate flag and go to the next element. Setting the flags for capital of number makes it easier to identify if we’re dealing with an alphabet or digit later on. The next step was check to see if the element was a space; if so, add it to the returned string and unset the num flag  given the problem context. 
We can then check the punctuation as it doesn’t matter if the number or capital flags are set (ie. 1? Or a? of HEY!).  Convert it and then continue to next element. I then do a check to see if the element is an alphabet or digit by checking the state of the number flag. If it is false, then alphabet, else digit. Within the block where character is alphabet, check to see the capital flag is set and convert the converted element to uppercase and unset the capital flag. If the number flag is set, then convert to English and add to string. I am not doing extra checking for the context given that I included the ‘.’ Which I treated as “decimal follows” in my digit mapping.
After iterating through each element, the final converted string is returned.

engToBrailleTranslator.ts:

A similar approach was used as mentioned above, however additional checks were necessary to understand the context of ‘.’
There are 2 flags to identify when we have numbers and when we have a decimal because string could be whole numbers or floating point (1.2 or .1 for example). Iterating over the array by splitting the English sentence, I initially check if the element is a digit. This is done by checking the char is in the digit to braille map and we don’t currently have a decimal number. Since my digit to braille map and vice versa has the ‘.’ Character need to check its context. 
If the character coming in is ‘,’ and the next char isn’t a digit that means the char MUIST be a period, in which case convert it, add it to the string and continue to the next element. If the char isn’t ‘,’ set the number and number identifier flags and add the converted char to the returned string. 
For the flags to be unset, there must be a space. So we check for that. If the element was a space, add converted character to returned string and unset fhe number and number identifier flags.
From there I went to check punctuation where I do another contextual check on ‘.’ Because if the number identifier flag is set then we already have a number so it dones’t make sense to add the number follows identifier again. However if it is not ‘.’ Then it’s a regular punctuation. Convert to braille and then add to the returned string.
Then I check to see if the char is an alphabet by checking the number flag. If the char is an alphabet check if it is capital using Unicode check and then convert it to its braille equivalent. Depending on if the letter was capital or not add the capitalized or current char to the returned string. Otherwise we have a digit, in which case convert to braille equivalent and add to the returned string.
After iterating over all elements, the converted string is returned.
