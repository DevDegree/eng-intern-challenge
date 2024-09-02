------------------------
Key assumptions
------------------------
1) Braille inputs are at least 6 characters long and can only contain 'O' and '.' in any combination as long as the minimum string length is satisfied
2) Based on research the '<', '>' and '.' (depending on situation) are used in the context of numbers. As a result when they are processed, the NUMBERFOLLOWS symbol preceeds them
3) When the NUMBERFOLLOWS symbol appears it is assumed that the following characters are strictly numbers, with the exception being punctuations (ie. "1." OR "is it only 1?")
   However, '.' depends on context and must be checked
4) When there is a space, the following characters are assumed to be anything unless the NUMBERFOLLOWS appears again
5) If a char = '.' but the next char is not a digit, then it is treated as a period. Otherwise it is treated as a decimal (will be preceeded by NUMBERFOLLOWS braille symbol )
   ie. If something like 1.2, then NUMBERFOLLOWS comes before the digit 1
       If something like .1, then NUMBERFOLLOWS comes before the dot 

------------------------
Approach
------------------------
Since we are given the english and braille mappings, it made sense to use a hashmap. Although it may be memory intensive, the fast retreival in O(1) is a good tradeoff if the application was scaled compared to using other data structures like arrays. 

Hashmaps and constants used by the translators were saved in separate files and imported as required for organization and keeping the code clean. 

Any functions that were common between the translators were treated as library functions and placed in a separate file which were imported for use.

In order to solve this problem I decided to break the problem into smaller pieces  that were easier to read and help with debugging. When an argument is passed into my translator functions, we check to see if it's braille based on the assumptions. In case of either function, an array is passed to the corresponding translators. Arrays were used for readability and ease to work with. For braille to english, an array where each element had 6 chars were passed and for english to braille the sentence was simply split.

    
brailleToEngTranslator.ts:=>

The function was structured to iterate over each braille array element and initially check if the CAPITALFOLLOWS or NUMBERFOLLOWS were detected to help set isCapital and isNum flags. Besides the trivial checks, they also help in identifying if the element is an alphabet or digit. These flags would be unset when a space is encountered. Punctuation doesn't care if we're dealing with numbers, except for '.' which was added to the digit to braille mapping to reduce additional contextual checks. In this process the equivalent english string is being updated and returned at the end.

engToBrailleTranslator.ts:=> 

The overall structure is similar to the brailleToEngTranslator, however a number flag is used only. The added piece is the logic to check the context if char = '.' In this process the equivalent english string is being updated and returned at the end. 

Overall I tried keeping the code structured and easily readable by keeping ismilar logic together or by breaking down large code blocks into smaller re-usable pieces. 


------------------------
Interesting Observation:
------------------------
From my research I noticed that leters k-t have a 'O' at position 3 of the braille cell and letters u-z have a 'O' at position 3 and 6 using a-j as the root characters. It'd' be interesting to see if translations could be done using this knowledge. In terms of scalability it may be more efficient because we have less entries in the hashmaps, however the process of infering will require cmore complex logic...

