import subprocess


# Tests translator.py with a set of arguments and an expected result
def tester(args, expected : str) -> None:
    command = ["python3", "translator.py"] + args
    
    # Run command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check expected is the same as result
    assert(result.stdout.strip() == expected)


if __name__ == '__main__':
    # Test cases
    tester(["Hello", "world"], ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..")
    tester([".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."], "Hello world")
    tester(["42"], ".O.OOOOO.O..O.O...")
    tester([".O.OOOOO.O..O.O..."], "42")
    tester([".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."], "Abc 123")
    tester(["Abc 123"], ".....OO.....O.O...OO...........O.OOOO.....O.O...OO....")
    tester(["H3"], ".....OO.OO...O.OOOOO....")
    tester([".....OO.OO...O.OOOOO...."], "H3")
    tester(["H42", "H"], ".....OO.OO...O.OOOOO.O..O.O..............OO.OO..")
    tester([".....OO.OO...O.OOOOO.O..O.O..............OO.OO.."], "H42 H")
    tester(["42", "42", "42", "42"], ".O.OOOOO.O..O.O..........O.OOOOO.O..O.O..........O.OOOOO.O..O.O..........O.OOOOO.O..O.O...")
    tester([".O.OOOOO.O..O.O..........O.OOOOO.O..O.O..........O.OOOOO.O..O.O..........O.OOOOO.O..O.O..."], "42 42 42 42")
    tester(["aA"], "O..........OO.....")
    tester(["O..........OO....."], "aA")
    tester(["O..........OO....."], "aA")
    tester(["O..........OO....."], "aA")
    tester(["O.............................O....."], "a    a")
    tester([".O.OOO.OOO...OOO.."], "00")
    tester(["00"], ".O.OOO.OOO...OOO..")
    tester(["00", "00"], ".O.OOO.OOO...OOO.........O.OOO.OOO...OOO..")
    tester([".O.OOO.OOO...OOO.........O.OOO.OOO...OOO.."], "00 00")
    tester(["a", "b", "c", "d", "e", "f"], "O...........O.O.........OO..........OO.O........O..O........OOO...")
    tester(["O...........O.O.........OO..........OO.O........O..O........OOO..."], "a b c d e f")
    tester(["g", "h", "i", "j", "k", "l"], "OOOO........O.OO.........OO..........OOO........O...O.......O.O.O.")
    tester(["OOOO........O.OO.........OO..........OOO........O...O.......O.O.O."], "g h i j k l")
    tester(["m", "n", "o", "p", "q", "r", "s", "t", "u"], "OO..O.......OO.OO.......O..OO.......OOO.O.......OOOOO.......O.OOO........OO.O........OOOO.......O...OO")
    tester(["OO..O.......OO.OO.......O..OO.......OOO.O.......OOOOO.......O.OOO........OO.O........OOOO.......O...OO"], "m n o p q r s t u")
    tester(["v", "w", "x", "y", "z"], "O.O.OO.......OOO.O......OO..OO......OO.OOO......O..OOO")
    tester(["O.O.OO.......OOO.O......OO..OO......OO.OOO......O..OOO"], "v w x y z")
    tester(["0123456789"], ".O.OOO.OOO..O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO...")
    tester([".O.OOO.OOO..O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO..."], "0123456789")
    tester(["H3", "a", "42"], ".....OO.OO...O.OOOOO..........O............O.OOOOO.O..O.O...")
    tester([".....OO.OO...O.OOOOO..........O............O.OOOOO.O..O.O..."], "H3 a 42")
    tester(["a", "42"], "O............O.OOOOO.O..O.O...")
    tester(["O............O.OOOOO.O..O.O..."], "a 42")
