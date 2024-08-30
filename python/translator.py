import sys
#your representation of alphabet-strings are not accurate, especially with numbers. Hence tests are not accurate, 
#Also working with our local machine, using subprocess in test file is not a decent practice, it may result(it did) with permission,
#environment variable or working directory errors. 
bte = {
    "O.....": ("a", "1"), "O.O...": ("b", "2"), "OO....": ("c", "3"), "OO.O..": ("d", "4"), "O..O..": ("e", "5"), 
    "OOO...": ("f", "6"), "OOOO..": ("g", "7"), "O.OO..": ("h", "8"), ".OO...": ("i", "9"), ".OOO..": ("j", "0"),
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y", "O..OOO": "z",
    ".....O": "Cap", ".O.OOO": "Num", "......": " ", ".O...O": "Dec", 
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!", "..OO..": ":", "..O.O.": ";",  ".O..O.": "/", 
    ".OO..O": "<",  "O.O..O": "(", ".O.OO.": ")"
}


etb = {}

for k, v in bte.items():
    if isinstance(v, str):
        etb[v] = k  
    elif isinstance(v, tuple):
       
        if v[0] not in etb:
            etb[v[0]] = k 
        if v[1] not in etb:
            etb[v[1]] = k 
etb.update({ ">": "O..OO."})
etb.update({"-": "OOOO.."})

def solve(s):
    res = []
    if(all(c in "O." for c in s) and len(s) % 6 == 0): 
        i = 0
        cap_next = False
        num_next = False
        while i < len(s):
            bc = s[i:i+6]
            if bc == '.....O': 
                cap_next = True
                i += 6
                continue
            if bc == '.O.OOO': 
                num_next = True
                i += 6
                continue
            if bc == '......': 
                num_next = False
                res.append(' ')
                i += 6
                continue
            ec = bte.get(bc)  
            if cap_next:
                ec = (ec[0].upper(), ec[1])
                cap_next = False
            if num_next:
                res.append(ec[1])  
            else:
                res.append(ec[0]) 
            i += 6
    else: 
        number_sequence = False
        for c in s:
            if c.isupper():  
                res.append(etb["Cap"])
                c = c.lower()
            if c.isdigit():  
                if not number_sequence:
                    res.append(etb["Num"]) 
                    number_sequence = True
                res.append(etb[c])  
            elif c == ' ':
                number_sequence = False 
                res.append(etb[' '])
            else:
                res.append(etb.get(c))  
    return ''.join(res)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inp = ' '.join(sys.argv[1:])
        output = solve(inp)
        print(output)
    else:
        print("No input")
        sys.exit(1)

