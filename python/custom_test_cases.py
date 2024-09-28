TESTS = [
  # tests from examples:
  { 
    "english": "Hello world",
    "braille": ".....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O.."
  },
  { 
    "english": "42",
    "braille": ".O.OOOOO.O..O.O..."
  },
  { 
    "english": "4.2",
    "braille": ".O.OOOOO.O...O...OO.O..."
  },
  { 
    "english": ".2",
    "braille": "..OO.O.O.OOOO.O..."
  },
  { 
    "english": "Abc 123",
    "braille": ".....OO.....O.O...OO...........O.OOOO.....O.O...OO...."
  },
  { 
    "english": "Abc 123 xYz",
    "braille": ".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO"
  # Basic alphabet test
  },
  {
    "english": "abcdefghijklmnopqrstuvwxyz",
    "braille": "O.....O.O...OO....OO.O..O..O..OOO...OOOO..O.OO...OO....OOO..O...O.O.O.O.OO..O.OO.OO.O..OO.OOO.O.OOOOO.O.OOO..OO.O..OOOO.O...OOO.O.OO.OOO.OOO..OOOO.OOOO..OOO"
  },  
  # Capitalization test
  {
    "english": "HELLO World",
    "braille": ".....OO.OO.......OO..O.......OO.O.O......OO.O.O......OO..OO............O.OOO.OO..OO.O.OOO.O.O.O.OO.O.."
  }
]