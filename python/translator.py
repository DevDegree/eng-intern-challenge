'''Hello and welcome to my braille translator program! :) Something that I find helps when I'm coding
is writing step-by-step instructions to myself on how to build it. In a general circumstance,
I would take these out and leave simple comments for functionality, but I figured that it might let you
into my thought process of how I went about solving it :) Thanks! :)'''

# (1) Accept the input from the user
user_input = input()

# (2) Determine if it's braille or english
type = 'braille'
# Does it contain any other characters than O and .: If so it's english
for char in user_input:
    if char != 'O' and char != '.':
        type = 'english'

"""# (3) If English, pass to braille translator...
if type == 'english':
  english_translator(user_input)"""
  
"""# (4) If Braille, pass to English translator...
if type == 'braille':
  braille_translator(user_input)"""

if type == 'braille':
  # Braille
  # Split up into segments of 6 dots and add to a list to cycle through
  
  conversation_table = {".....O" : "cap", ".O.OOO" : "num", "......" : " ", "O....." : "a", "O.O..." : "b", "OO...." : "c", "OO.O.." : "d", "O..O.." : "e", "OOO..." : "f", "OOOO.." : "g", "O.OO.." : "h", ".OO..." : "i", ".OOO.." : "j", "O...O." : "k",
      "O.O.O." : "l", "OO..O." : "m", "OO.OO." : "n", "O..OO." : "o", "OOO.O." : "p", "OOOOO." : "q", "O.OOO." : "r", ".OO.O." : "s", ".OOOO." : "t", "O...OO" : "u", "O.O.OO" : "v", ".OOO.O" : "w", "OO..OO" : "x", "OO.OOO" : "y", "O..OOO" : "z", 
      "..OO.O" : ".", "..O..." : ",", "..O.OO" : "?", "..OOO." : "!", "..OO.." : ":", "..O.O." : ";", "....OO" : "-", ".O..O." : "/", ".OO..O" : "<", "O.O..O" : "(", ".O.OO." : ")"}
  
  # Start at first character
  n = 0
  num_of_braille_letters = len(user_input)/6
  
  list_of_braille_letters = []

  i = 0
  while len(list_of_braille_letters) < num_of_braille_letters:
      new_segment = user_input[n:n+6]
      list_of_braille_letters.append(new_segment)
      n = n + 6
    
  #Now, translate each segment, based on the dictionary
  translated_list = []
  for letter in list_of_braille_letters:
      translated_letter = conversation_table[letter]
      translated_list.append(translated_letter)

  number_dict = {"a" : "1", "b" : "2", "c" : "3", "d" : "4", "e": "5", "f": "6", "g" : "7", "h" : "8", "i" : "9", "j" : "0", "o": ">"}
  undercase = True
  num_follows = False
  refined_list = []
  for new_letter in translated_list:
      if new_letter == ' ':
          num_follows = False
      if num_follows == True:
          refined_list.append(number_dict[new_letter])
      elif undercase == False:
          refined_list.append(new_letter.upper())
          undercase = True
      elif new_letter == 'cap':
          undercase = False
      elif new_letter == 'num':
          num_follows = True
      else:
          refined_list.append(new_letter)
        
  final_translation = ''       
  for char in refined_list:
      final_translation = final_translation + char
  print(final_translation)

if type == 'english':
  # English Translator...
  # (5) Create a dictionary set up key (English): value (Braille)
  # conversation_table = dict('a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..', 'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...', 'j':'.OOO..', 'k': 'O...O.', 'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.', 'p':'OOO.O.', 'q':'OOOOO.')
  # Remember to do rest of characters!
  # (6) Use a loop to go through each character and add put the braille string to output string
  # Remember: Things need precidence...

  translation_table = {" " : "......", "a" : "O.....", "b" : "O.O...", "c" : "OO....", "d" : "OO.O..", "e" : "O..O..", "f" : "OOO...", "g" : "OOOO..", "h" : "O.OO..", "i" : ".OO...", "j" : ".OOO..", "k" : "O...O.", 
      "l" : "O.O.O.", "m" : "OO..O.", "n" : "OO.OO.", "o" : "O..OO.", "p" : "OOO.O.", "q" : "OOOOO.", "r" : "O.OOO.", "s" : ".OO.O.", "t" : ".OOOO.", "u" : "O...OO", "v" : "O.O.OO", "w" : ".OOO.O", "x" : "OO..OO",
      "y" : "OO.OOO", "z" : "O..OOO", "." : "..OO.O", "," : "..O...", "?" : "..O.OO", "!" : "..OOO.", ":" : "..OO..", ";" : "..O.O.", "-" : "....OO", "/" : ".O..O.", "<" : ".OO..O", ">" : "O..OO.", "O.O..O" : "(", ".O.OO." : ")"}

  translation_list = []
  list_of_input = []
  for char in user_input:
      list_of_input.append(char)
  num_to_let = {"1" : "a", "2" : "b", "3" : "c", "4" : "d", "5" : "e", "6" : "f", "7" : "g", "8" : "h", "9" : "i", "0" : "j"}
  first_num = True
  for letter in list_of_input:  
      if letter.isupper():
          # Add capital follows before letter
          translation_list.append(".....O")
          letter = letter.lower()
      if letter.isdigit():
          # Add number follows before letter
          if first_num == True:
              translation_list.append(".O.OOO")
          first_num = False
          # Number is also set as the corresponding letter
          letter = num_to_let[letter]
      if letter == " ": 
          first_num = True
      translation_list.append(translation_table[letter])
    
  output_string = ''
    
  for char in translation_list:
      output_string = output_string + char
  print(output_string)


  
