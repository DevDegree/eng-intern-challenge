# Go Instructions

## To run the CLI application and unit tests:
- Go into the `go` directory
```
cd go
```
- To translate English or Braille (replace `<text>` with English or Braille text to be translated):
```
go run translator.go <text>
```
- To run unit tests:
```
go test translator_test.go
```

## Assumptions:
- [Numbers can be terminated by a letter](https://www.nationalbraille.org/forums/topic/letters-following-numbers/)
- [Incorrect test cases per Issue #6](https://github.com/DevDegree/eng-intern-challenge/issues/6)

## References:
- [Exercise book to make sure I know Braille :)](https://cnib.ca/sites/default/files/2021-09/Reading-Uncontracted-Braille-2014_0.pdf)

## Notes:

Example from book:
- `.O.OOO -> number follows`
- `OO.O.. -> 4`
- `.OOOO. -> t (number is terminated by a letter outside of a-j)`
- `O.OO.. -> h`

Example:
- `.....O -> capital follows`
- `O.OO.. -> H`
- `.O.OOO -> number follows`
- `OO.... -> 3`
- `O.O.O. -> l`
- `.....O -> capital follows`
- `O.O.O. -> L`
- `.O.OOO -> number follows`
- `.OOO.. -> 0`

## Limitations:

CLI program limitations via example:
- `5ft -> .O.OOOO..O..OOO....OOOO.`
    - Should actually be:
        - `.0.000 -> number follows`
        - `O..O.. -> 5`
        - `...O.O -> grade 1 indicator (avoid misread of lowercase a-j)`
        - `OOO... -> f`
        - `.OOOO. -> t`
- `.O.OOOO..O..OOO....OOOO. -> 56t`
