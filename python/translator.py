import sys
s = []
i = 1

st = " ".join(sys.argv[1:])
engl_dict = {      'a': 'O.....', 
                   'b': 'O.O...',
                   'c': 'OO....',
                   'd': 'OO.O..',
                   'e': 'O..O..',
                    'f': 'OOO...',
                    'g': 'OOOO..',
                    'h': 'O.OO..',
                    'i': '.OO...',
                    'j': '.OOO..',
                    'k': 'O...O.',
                    'l': 'O.O.O.',
                    'm': 'OO..O.',
                    'n': 'OO.OO.',
                    'o': 'O..OO.',
                    'p': 'OOO.O.',
                    'q': 'OOOOO.',
                    'r': 'O.OOO.',
                    's': '.O.OO.',
                    't': '.OOOO.',
                    'u': 'O...OO',
                    'v': 'O.O.OO',
                    'w': '.OOO.O',
                    'x': 'OO..OO',
                    'y': 'OO.OOO',
                    'z': 'O..OOO',
                    ' ': '......',
                    'capitals': '.....O',
                    'numbers': '.O.OOO',
                    '.': '..OO.O',
                    ',': '..O...',
                    '?': '..O.OO',
                    '!': '..OOO.',
                    ":": '..OO..',
                    ';': '..O.O.',
                    '-': '....OO',
                    '/': '.O..O.',
                    '<': '.00..O',
                    ">": "O.O.O.",
                    "(": "OO...O",
                    ")": ".OO.O.",
                    }

num_dict = {'1': 'O.....',  # 1
                '2': 'O.O...',  # 2
                '3': 'OO....',  # 3
                '4': 'OO.O..',  # 4
                '5': 'O..O..',  # 5
                '6': 'OOO...',  # 6
                '7': 'OOOO..',  # 7
                '8': 'O.OO..',  # 8
                '9': '.OO...',  # 9
                '0': '.OO0..',  # 0
                }
braile_dic = {}
for key, value in engl_dict.items():
    braile_dic[value] = key
bnum_dict = {}
for key, value in num_dict.items():
    bnum_dict[value] = key
capitals = False
nums = False

res = ""
if st[:6] in braile_dic:
    for i in range(0, len(st), 6):
        if capitals:
            res += braile_dic[st[i:i+6]].upper()
            capitals = False
            continue
        if nums:
            res += bnum_dict[st[i:i+6]]
            continue
        if braile_dic[st[i:i+6]] == "capitals":
            capitals = True
        elif braile_dic[st[i:i+6]] == "numbers":
            nums = True
        elif braile_dic[st[i:i+6]] == " ":
            nums = False
            res += " "
        else:
            res += braile_dic[st[i:i+6]]
else:
    for i in range(0, len(st)):
        if st[i].isupper():
            res += engl_dict["capitals"]
            res += engl_dict[st[i].lower()]
        elif st[i].isdigit():
            if nums == False:
                res += engl_dict["numbers"]
                nums = True
            res += num_dict[st[i]]
        elif st[i] == " ":
            res += engl_dict[" "]
            nums = False
        elif st[i] in engl_dict:
            res += engl_dict[st[i]]
        elif st[i] in num_dict:
            res += num_dict[st[i]]
        else:
            res += st[i]
print(res)


        



