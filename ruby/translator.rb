
# create the hash of braille to english
braille_hash = {
  "a" => 'O.....',
  "b" => 'O.O...',
  "c" => 'OO....',
  "d" => 'OO.O..',
  "e" => 'O..O..',
  "f" => 'OOO...',
  "g" => 'OOOO..',
  "h" => 'O.OO..',
  "i" => '.OO...',
  "j" => '.OOO..',
  "k" => 'O...O.',
  "l" => 'O.O.O.',
  "m" => 'OO..O.',
  "n" => 'OO.OO.',
  "o" => 'O..OO.',
  "p" => 'OOO.O.',
  "q" => 'OOOOO.',
  "r" => 'O.OOO.',
  "s" => '.OO.O.',
  "t" => '.OOOO.',
  "u" => 'O...OO',
  "v" => 'O.O.OO',
  "w" => '.OOO.O',
  "x" => 'OO..OO',
  "y" => 'OO.OOO',
  "z" => 'O..OOO',
  " " => '......',
}
# create the hash of english to braille
english_hash = braille_hash.invert

# Create an evaluator to determine if english or braille
def braille_checker?(input_string)
  input_string.include?(".")
end

# If english, translate to braille
def english_translator(input_string); end
# If braille, translate to english
def braille_translator(input_string); end

# MAKE SURE TO REMEMBER to account for number follows and capital letter follows

# Program must work at runtime
def run(input_string)
  braille_checker?(input_string) ? braille_translator(input_string) : english_translator(input_string)
end

run(ARGV.join(" "))
