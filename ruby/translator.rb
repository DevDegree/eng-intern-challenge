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
  'o.....' => '1',
  'o.o...' => '2',
  'oo....' => '3',
  'oo.o..' => '4',
  'o..o..' => '5',
  'ooo...' => '6',
  'oooo..' => '7',
  'o.oo..' => '8',
  '.oo...' => '9',
  '.ooo..' => '0'
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

def eng_to_braille(input_value, eng_to_braille_hash, num_to_braille_hash)
  p "eng to braille"
  index = 0
  output = ""
  while index < input_value.length
    if input_value[index] =~ /[A-Z]/
      output += eng_to_braille_hash["capital follows"] + eng_to_braille_hash[input_value[index].downcase]
    elsif input_value[index] =~ /[0-9]/
      p input_value[index] 
      output += eng_to_braille_hash['number follows']  + num_to_braille_hash[input_value[index]]
    else
      output = output + eng_to_braille_hash[input_value[index]]
    end
    index += 1
  end
  p output
end

# .o.oooo.o...o.oo........ooo.o
# .o.ooo.ooo.o.......ooo.o.....ooo..oo.o.ooooo.o..
def braille_to_eng(input_value, braille_to_eng_map, braille_to_num_map)
  output = ""
  is_n = false
  input_index = 0
  while input_index < input_value.length
    if braille_to_eng_map[input_value[input_index,6]] == 'number follows'
      is_n = true
      input_index += 6
    end
    if braille_to_eng_map[input_value[input_index,6]] == ' '
      is_n = false
      # input_index += 6
    end
    # elsif braille_to_eng_map[input_value[input_index,6]] == '......'
    #   is_n = false
    #   p braille_to_eng_map[input_value[input_index,6]]
    # end
    # if is_n
    #   output = output + braille_to_num_map[input_value[input_index,6]]
    # end
    if is_n 
      p braille_to_num_map[input_value[input_index,6]]
      # output = output + braille_to_num_map[input_value[input_index,6]]
    else
      if braille_to_eng_map[input_value[input_index,6]] == 'capital follows'
        output = output + braille_to_eng_map[input_value[input_index + 6,6]].upcase
        input_index += 6
      else
        output = output + braille_to_eng_map[input_value[input_index,6]]
      end
    end
    # if braille_to_eng_map[input_value[input_index,6]] == 'capital follows'
    #   output = output + braille_to_eng_map[input_value[input_index + 6,6]].upcase
    #   input_index += 6
    # elsif is_n == true
    #   p braille_to_num_map[input_value[input_index,6]]
    #   output = output + braille_to_num_map[input_value[input_index,6]]
    # else
    #   output = output + braille_to_eng_map[input_value[input_index,6]]
    # end
    input_index += 6
  end
    
  p output
end


# ##### main 
input_value = gets.chomp 

if check_braille(input_value)
  braille_to_eng(input_value, braille_to_eng_hash, braille_to_num_hash)
else
  eng_to_braille(input_value, eng_to_braille_hash, num_to_braille_hash)
end
# index =0
# newoutput= ""


# while index < i.length
#   newoutput = newoutput +  eng_to_braille_hash[i[index]]
#   index += 1
# end
# p newoutput







