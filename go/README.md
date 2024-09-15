# Go Instructions

## Run
```bash
$ go run ./translator.go Abc 123 xYz
.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO
```

## Build
```bash
$ go build ./translator.go
```

## Usage
```bash
$ ./translator "Abc 123 xYz"
.....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO

$ ./translator ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
Hello world

$ ./translator Hello world
.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..

$ ./translator 42
.O.OOOOO.O..O.O...

$ ./translator .O.OOOOO.O..O.O...
42

$ ./translator .....OO.....O.O...OO...........O.OOOO.....O.O...OO....
Abc 123

$ ./translator Abc 123
.....OO.....O.O...OO...........O.OOOO.....O.O...OO....
```

## Test
```bash
$ go test
```
