import csv


def setup_dictionary():
    library =[]
    with open('./data/EngToBraille.csv', 'r') as file:
        library= [tuple(row.strip().split(',')) for row in file]
        library.append((" ","......"))
    return library

