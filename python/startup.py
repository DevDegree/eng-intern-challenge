import csv


def setupDict():
    library =[]
    with open('./data/EngToBraille.csv', 'r') as file:
        library= [tuple(row.strip().split(',')) for row in file]
        #if library[0] == "space":
        #    library[0] = ' '
        library.append((" ","......"))
    return library

