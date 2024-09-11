import translatorUtility
import sys

# create an instant of the translator with the default input language set to Braille
translatorEngine = translatorUtility.translator(False, False, "Braille")

# find the length of the input text
nInputLength = len(sys.argv)

# find the input text from the run-time arguments
sText = ""
for iArg in range(1, nInputLength):
    # if we have multiple words we need to insert a space between them
    if (len(sText) > 0):
        sText = sText + " "
    sText = sText + sys.argv[iArg]
    
# call the translateString method to find the translated text
sresult = translatorEngine.tranlateString(sText)

# output the translated text back to the terminal
print(sresult)

