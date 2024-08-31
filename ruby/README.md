# Ruby Instructions

## Overview

`translator.rb` was written with the version of ruby stated in the `Dockerfile`. For a reproducible environment, you can run:

```
docker-compose build
docker-compose run app sh
```

This will allow you to run the script in the same environment it was developed.

## Assumptions

For braille inputs:

-   invalid braille will cause translator to default to assuming the input is English
-   input is only valid if it contains only `O` and `.`. Spaces makes the input invalid.
-   valid input has a length divisible by 6 because each braille letter is a 2x3

For English inputs:

-   valid input includes the characters of the alphabet (both capitalize and non-capitalized), numbers (0-9), and the symbols listed in the instruction README
-   Capitalization only affect the letter directly following it
-   negative numbers follows the following format: `{minus symbol braille}{number follow brailles}{number braille}`
-   unknown letters gets omitted in the output
