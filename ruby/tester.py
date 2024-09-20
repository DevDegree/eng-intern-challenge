import subprocess
import random as r
#print(subprocess.run(['ruby', 'translator.rb', 'test'], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip())

def generateRandomStr(inlen):
    out = ""
    for i in range(inlen):
        out += r.choice(list("The quick brown fox jumps over the lazy dog") + list("The quick brown fox jumps over the lazy dog".capitalize()) + list("1234567890.,?!:;-/<>() "))

    return out

def test(its):
    for i in range(its):
        testp = generateRandomStr(50)
        inv = subprocess.run(['ruby', 'translator.rb', testp], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
        outv = subprocess.run(['ruby', 'translator.rb', inv], stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()

        if outv in testp:
            print("Passed", i, "of", its)
        else:
            print("Failed", i, "of", its)
            print(testp)
            print("Expected:", testp, "Actual:", outv)


test(100)