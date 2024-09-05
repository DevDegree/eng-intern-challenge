# Translator app that converts english to braille and viceversa

# Problem break up

  #1 Read input string and classify as eng or braille
  #2 create hash for mapping alphabets, numbers and other patterns.
  #3 Read in input alphabet string and convert to braille . Check output
  #4 Add edge cases like capital letter and numbers. check ouput
  #5 Read in braille charaters and convert to letters. Check output
  #6 Add edge case for capital letters. Check output
  #7 Add edge case for numbers. Check output
  


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
# create reverse hash
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
# create reverse hash
num_to_braille_hash = braille_to_num_hash.invert

# check if input is braille or english
def check_braille(input_value)
  if input_value.match?(/^[o.]+$/) == true
    true
  else 
    false
  end
end

# Translate English to Braille
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

# Translate Braille to English

def braille_to_eng(input_value, braille_to_eng_map, braille_to_num_map)
  output = ""
  is_num = false
  index = 0
  while index < input_value.length
    braille_string = input_value[index,6]
    if braille_to_eng_map[braille_string] == 'number follows'
      is_num = true
    elsif braille_to_eng_map[braille_string] == 'capital follows'
      output = output + braille_to_eng_map[input_value[index + 6,6]].upcase
      index += 6
    else
      if braille_string == '......'
        is_num = false
      end
      if is_num 
        output = output + braille_to_num_map[input_value[index,6]]
      else
        output = output + braille_to_eng_map[braille_string]
      end    
    end 
    index += 6
  end
    
  p output
end


# ##### main 

# get the input string
input_value = ARGV.join(" ")

# check if string is Braille or English and then call the translator method accordingly 
if check_braille(input_value)
  braille_to_eng(input_value, braille_to_eng_hash, braille_to_num_hash)
else
  eng_to_braille(input_value, eng_to_braille_hash, num_to_braille_hash)
end








