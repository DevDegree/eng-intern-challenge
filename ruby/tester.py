import subprocess
import random as r
#print(subprocess.run(['ruby', 'translator.rb', 'test'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip())

def generateRandomStr(inlen):
    out = ""
    for i in range(inlen):
        out += r.choice(list("The quick brown fox jumps over the lazy dog") + list("The quick brown fox jumps over the lazy dog".capitalize()) + list("1234567890.,?!:;-/ "))

    return out

def test(its):
    for i in range(its):
        testp = generateRandomStr(r.randint(0,100))
        inv = subprocess.run(['ruby', 'translator.rb', testp], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip().replace("\x00", "")
        outv = subprocess.run(['ruby', 'translator.rb', inv], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip().replace("\x00", "")

        print("Test case:",testp)
        if outv in testp:
            print("Passed", i, "of", its)
        else:
            print("Failed", i, "of", its)
            print("Expect:", list(testp), "\nActual:", list(outv))


test(100)