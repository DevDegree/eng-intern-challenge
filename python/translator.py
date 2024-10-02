import sys

#dictionaries
Alphabet_Braille_Dict={'a':'O.....','b':'O.O...','c':'OO....','d':'OO.O..','e':'O..O..','f':'OOO...','g':'OOOO..','h':'O.OO..','i':".OO...",'j':'.OOO..','k':'O...O.','l':'O.O.O.','m':'OO..O.','n':'OO.OO.','o':'O..OO.','p':'OOO.O.','q':'OOOOO.','r':'O.OOO.','s':'.OO.O.','t':'.OOOO.','u':'O...OO','v':'O.O.OO','w':'.OOO.O','x':'OO..OO','y':'OO.OOO','z':'O..OOO'}
Braille_Alphabet_Dict= dict((v,k) for k,v in Alphabet_Braille_Dict.items())

Next_Braille_Dict={'capNext':'.....O','decimalNext':'.O...O','numberNext':'.O.OOO'}
Braille_Next_Dict=dict((v,k) for k,v in Next_Braille_Dict.items())
             
Number_Braille_Dict={'1':'O.....','2':'O.O...','3':'OO....','4':'OO.O..','5':'O..O..','6':'OOO...','7':'OOOO..','8':'O.OO..','9':'.OO...','0':'.OOO..'}
Braille_Number_Dict=dict((v,k) for k,v in Number_Braille_Dict.items())

Punct_Braille_Dict={'.':'..OO.O',',':'..O...','?':'..O.OO','!':'..OOO.',':':'..OO..',';':'..O.O.','-':'....OO','/':'.O..O.','<':'.OO..O','>':'O..OO.','(':'O.O..O',')':'.O.OO.',' ':'......'}
Braille_Punct_Dict=dict((v,k) for k,v in Punct_Braille_Dict.items())

#English to Braille 
def English_Braille_Translate(input_ls):
  '''Take an English Sentence input_ls and return the translated Braille sentence'''
  English_Sentence=' '.join(input_ls)
  Braille_Sentence=''
  for i in range(len(English_Sentence)):
    element=English_Sentence[i]
    #alphabet
    if element.isalpha():
      if element.isupper():
        Braille_Sentence+=Next_Braille_Dict['capNext']
        element=element.lower()
      Braille_Sentence+=Alphabet_Braille_Dict[element]
    #punctuation
    elif element in Punct_Braille_Dict:
      Braille_Sentence+=Punct_Braille_Dict[element]
    #numbers
    elif element.isdigit():
      #number at first place
      if i==0 or not(English_Sentence[i-1].isdigit()):
        Braille_Sentence+=Next_Braille_Dict['numberNext']
      Braille_Sentence+=Number_Braille_Dict[element]

  return Braille_Sentence

#Braille to English
def Braille_English_Translate(input_ls):
  '''Take a Braille sentence input_ls and return the translated English sentence'''
  Braille_Sentence=''.join(input_ls)
  chunks, chunk_size = len(Braille_Sentence), len(Braille_Sentence)//int(len(Braille_Sentence)/6)
  Braille_Sentence=[ Braille_Sentence[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
  English_Sentence=''
  #switch for knowing whether it should be a number of alphabet
  number_on=False
  capital_on=False
  for i in range(len(Braille_Sentence)):
    belement=Braille_Sentence[i]
    #number comes next
    if belement == Next_Braille_Dict['numberNext']:
      number_on=True
    #number
    elif number_on and belement in Braille_Number_Dict:
      English_Sentence+=Braille_Number_Dict[belement]

    #space
    elif belement == Punct_Braille_Dict[' ']:
      if i>0 and Braille_Sentence[i-1] in Braille_Number_Dict:
        number_on=False
      English_Sentence+=Braille_Punct_Dict[belement]

    #next alphabet capital
    elif belement == Next_Braille_Dict['capNext']:
      capital_on=True

    #alpha
    elif belement in Braille_Alphabet_Dict:
      if capital_on:
        English_Sentence+=Braille_Alphabet_Dict[belement].upper()
        capital_on=False
      else:
        English_Sentence+=Braille_Alphabet_Dict[belement]

    #punctuation
    elif belement in Braille_Punct_Dict:
      English_Sentence+=Braille_Punct_Dict[belement]

  return English_Sentence

def translate():
  '''Take the input sentence from the terminal and return the translated Braille or English sentence'''
  Translated_Sentence=''
  input_ls=sys.argv[1:]
  input=''.join(input_ls)

  #braille input
  if len(input)%6==0 and ((input[:6] in Braille_Alphabet_Dict) or (input[:6] in Braille_Next_Dict) or (input[:6] in Braille_Number_Dict) or (input[:6] in Braille_Punct_Dict)):
    Translated_Sentence=Braille_English_Translate(input_ls)

  #english input
  else:
    Translated_Sentence=English_Braille_Translate(input_ls)
  return Translated_Sentence  

#main run
if __name__ == '__main__':
  ans=translate()
  print(ans)   