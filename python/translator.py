braille_alphabet = {'a':'o.....', 'b': 'o.o...','c': 'oo....','d': 'oo.o..','e': 'o.o...','f': 'ooo...','g': 'oooo..','h':'o.oo..','i': '.oo...','j':'.ooo..','k': 'o...o.','l': 'o.o.o.','m':'oo..o.','n': 'oo.oo.','o': 'o..oo.','p': 'ooo.o.','q': 'ooooo.','r': 'o.ooo.','s':'.oo.o.', 't': '.oooo.','u': 'o...oo','v': 'o.o.oo','w': '.ooo.o','x': 'oo..oo','y': 'oo.ooo','z': 'o..ooo','1':'o.....','2':'o.o...','3':'oo....','4':'oo.o..','5':'o..o..','6':'ooo...','7':'oooo..','8':'o.oo..','9':'.oo...','0':'.ooo..','capital follows':'.....o','decimal follows':'.o...o','number follows':'.o.ooo','.':'..oo.o',',':'..o...','?':'..o.oo','!':'..ooo.',':':'..oo..',';':'..o.o.','-':'....oo','/':'.o..o.','<':'.oo..o','>':'o..oo.','(':'o.o..o',')':'','space':'......'}

#figure out if its English or Braille
string = "hi"
translation = ""
stop = False
index = 0
length = len(string)
while not stop and index < length:
    if(string[index] == '.'):
        print('this is a braille word')
        stop = True
    else:
        #print(string[index])
        addon_string = braille_alphabet.get(string[index])
        translation = translation + addon_string
    index = index + 1
   
print(translation)


