#--------------------alphabet------------------
A ={
    "char": "a",
    "braille": "O....."
}
B = {"char": "b",
    "braille": "O.O..."
     }
C = {"char": "c",
    "braille": "OO...."
     }
D = {"char": "d",
    "braille": "OO.O.."
     }
E = {"char": "e",
    "braille": "O..O.."
     }
F = {"char": "f",
    "braille": "OOO..."
     }
G = {"char": "g",
    "braille": "OOOO.."
     }
H = {"char": "h",
    "braille": "O.OO.."
     }
I = {"char": "i",
    "braille": ".OO..."
     }
J = {"char": "j",
    "braille": ".OOO.."
     }
K = {"char": "k",
    "braille": "O...O."
     }
L = {"char": "l",
    "braille": "O.O.O."
     }
M = {"char": "m",
    "braille": "OO..O."
     }
N = {"char": "n",
    "braille": "OO.OO."
     }
O = {"char": "o",
    "braille": "O..OO."
     }
P = {"char": "p",
    "braille": "OOO.O."
     }
Q = {"char": "q",
    "braille": "OOOOO."
     }
R = {"char": "r",
    "braille": "O.OOO."
     }
S = {"char": "s",
    "braille": ".OO.O."
     }
T = {"char": "t",
    "braille": ".OOOO."
     }
U = {"char": "u",
    "braille": "O...OO"
     }
V = {"char": "v",
    "braille": "O.O.OO"
     }
W = {"char": "w",
    "braille": ".OOO.O"
     }
X = {"char": "x",
    "braille": "OO..OO"
     }
Y = {"char": "y",
    "braille": "OO.OOO"
     }
Z = {"char": "z",
    "braille": "O..OOO"
     }
#-----------numbers----------
NUM_1 = {"char": "1",
    "braille": "O....."
         }
NUM_2 = {"char": "2",
    "braille": "O.O..."
         }
NUM_3 = {"char": "3",
    "braille": "OO...."
         }
NUM_4 = {"char": "4",
    "braille": "OO.O.."
         }
NUM_5 = {"char": "5",
    "braille": "O..O.."
         }
NUM_6 = {"char": "6",
    "braille": "OOO..."
         }
NUM_7 = {"char": "7",
    "braille": "OOOO.."
         }
NUM_8 = {"char": "8",
    "braille": "O.OO.."
         }
NUM_9 = {"char": "9",
    "braille": ".OO..."
         }
NUM_ZERO = {"char": "0",
    "braille": ".OOO.."
     }
#------------------------follows_marker----------
CAP_FOLLOWS = {
    "braille": ".....O"
     }
DECIMAL_FOLLOWS = {
    "braille": ".O...O"
     }
NUM_FOLLOWS = {
    "braille": ".O.OOO"
     }
#------------symbols-----------
PERIOD = {"char": ".",
    "braille": "..OO.O"
          }
COMMA = {"char": ",",
    "braille": "..O..."
     }
QUESTION_MRK = {"char": "?",
    "braille": "..O.OO"
     }
EXCLAMATION_MRK = {"char": "!",
    "braille": "..OOO."
     }
COLON = {"char": ":",
    "braille": "..OO.."
     }
SEMI_COLON = {"char": ";",
    "braille": "..O.O."
     }
DASH = {"char": "-",
    "braille": "....OO"
     }
SLASH = {"char": "/",
    "braille": ".O..O."
     }
LESS_THAN = {"char": "<",
    "braille": ".OO..O"
     }
GREATER_THAN = {"char": ">",
    "braille": "O..OO."
     }
LEFT_BRACKET = {"char": "(",
    "braille": "O.O..O"
     }
RIGHT_BRACKET = {"char": ")",
    "braille": ".O.OO."
     }
SPACE = {"char": " ",
    "braille": "......"
     }


LETTERS = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
NUMBERS = [NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9, NUM_ZERO]
SYMBOLS = [PERIOD, COMMA, QUESTION_MRK, EXCLAMATION_MRK, COLON, SEMI_COLON, DASH, SLASH, GREATER_THAN, LESS_THAN,
           LEFT_BRACKET, RIGHT_BRACKET, SPACE]
FOLLOW_MARKERS = [NUM_FOLLOWS, CAP_FOLLOWS, DECIMAL_FOLLOWS]
