#The purpose for the following file is to import a dictionary that is within a .csv file
#The dicitionary is a tuple, first element is the letter and the second element is the braille
#I chose to use a csv file because I have experience with working with them for ML/Kaggle purposes

import csv


def setup_dictionary():
    library =[]
    with open('./data/EngToBraille.csv', 'r') as file:
        library= [tuple(row.strip().split(',')) for row in file]

        #Was unsure how to have " " within the csv without it not working, therefore it is being appended into the code here
        library.append((" ","......"))
    return library

