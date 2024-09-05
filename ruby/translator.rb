# Translator app that converts english to braille and viceversa

# Problem break up

  #1 Read input string and clasiify as eng or braille
  #2 create hash for mapping alphabets, numbers and other patterns.
    # Read in input alphabet and output the braille pattern. 
  #3 Read in input alphabet string and convert to braille
  #4 Check input for uppercase alphabets and convert to braille by adding uppercase pattern before the alphabet
  #5 Check for number 0-9 and convert to braille pattern by adding number pattern before and space after the numbers
  #6 


# Create hash to store the braille pattern - alphabet/ special pattern mapping. Create a reverse hash to store Alphabet/special mapping - braille pattern mapping
# Create a number hash to store numbers from 0 - 9 and its braille petterns and a reverse hash to store mapping from pattern to number.
  
braille_to_eng_hash = {
  'o.....' => 'a',
  'o.o...' => 'b',
  'oo....' => 'c',
  'oo.o..' => 'd',
  'o..o..' => 'e',
  'ooo...' => 'f',
  'oooo..' => 'g',
  'o.oo..' => 'h',
  '.oo...' => 'i',
  '.ooo..' => 'j',
  'o...o.' => 'k',
  'o.o.o.' => 'l',
  'oo..o.' => 'm',
  'oo.oo.' => 'n',
  'o..oo.' => 'o',
  'ooo.o.' => 'p',
  'ooooo.' => 'q',
  'o.ooo.' => 'r',
  '.oo.o.' => 's',
  '.oooo.' => 't',
  'o...oo' => 'u',
  'o.o.oo' => 'v',
  '.ooo.o' => 'w',
  'oo..oo' => 'x',
  'oo.ooo' => 'y',
  'o..ooo' => 'z',

  '.....o' => 'capital follows',
  '.o...o' => 'decimal follows',
  '.o.ooo' => 'number follows',
  '..oo.o' => '.',
  '..o...' => ',',
  '...ooo' => '?',
  '..ooo.' => '!',
  '..oo..' => ':',
  '..o.o.' => ';',
  '....oo' => '-',
  '.o..o.' => '/',
  '.oo..o' => '<',
  # 'o..oo.' => '>',
  'o.o..o' => '(',
  '.o.oo.' => ')',
  '......' => ' '
}
eng_to_braille_hash = braille_to_eng_hash.invert

braille_to_num_hash = {
  'o.....' => 1,
  'o.o...' => 2,
  'oo....' => 3,
  'oo.o..' => 4,
  'o..o..' => 5,
  'ooo...' => 6,
  'oooo..' => 7,
  'o.oo..' => 8,
  '.oo...' => 9,
  '.ooo..' => 0
}
num_to_braille_hash = braille_to_num_hash.invert

 # i = gets.chomp
    # if i.match?(/^[o.]+$/) == true
    #   p "braille"
    # else 
    #   p "eng"
    # end

  
  #4


# pp braille_to_eng_hash
# pp eng_to_braille_hash
# pp braille_to_num_hash
# pp num_to_braille_hash
# i = gets.chomp
# p num_to_braille_hash[i.to_i]
# p braille_to_num_hash[i]

# check if input is braille or english
def check_braille(input_value)
  if input_value.match?(/^[o.]+$/) == true
      true
  else 
      false
  end
end

def eng_to_braille(input_value)
  p "eng to braille"
end

def braille_to_eng(input_value, braille_to_eng_map)
  # p "braille to eng"
  output = ""
  is_num = false
  is_capital = false
  input_index = 0
  while input_index < input_value.length
    if braille_to_eng_map[input_value[input_index,6]] == 'capital follows'
      output = output + braille_to_eng_map[input_value[input_index + 6,6]].upcase
      input_index += 6
    else
      output = output + braille_to_eng_map[input_value[input_index,6]]
    end
    input_index += 6
  end
    
  p output
end

input_value = gets.chomp 

if check_braille(input_value)
  braille_to_eng(input_value, braille_to_eng_hash)
else
  eng_to_braille(input_value)
end
# index =0
# newoutput= ""


# while index < i.length
#   newoutput = newoutput +  eng_to_braille_hash[i[index]]
#   index += 1
# end
# p newoutput







