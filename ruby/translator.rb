require_relative 'constants'
require_relative 'get_input_type'

def translate_english_to_braille(english_string)
  result = ""

  # check if capital
  # check if number
end


def main()
  input_type = get_input_type()

  if input_type == BRAILLE_TYPE
    puts "hello"
  else
    puts "world"
  end


end

main()
