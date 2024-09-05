CAPITAL_FOLLOWS = ".....O"
NUM_FOLLOWS = ".O.OOO"
SPACE = "......"

LETTER_TO_BR_DICT = {
    'a'=> "O.....",
    'b'=> "O.O...",
    'c'=> "OO....",
    'd'=> "OO.O..",
    'e'=> "O..O..",
    'f'=> "OOO...",
    'g'=> "OOOO..",
    'h'=> "O.OO..",
    'i'=> ".OO...",
    'j'=> ".OOO..",
    'k'=> "O...O.",
    'l'=> "O.O.O.",
    'm'=> "OO..O.",
    'n'=> "OO.OO.",
    'o'=> "O..OO.",
    'p'=> "OOO.O.",
    'q'=> "OOOOO.",
    'r'=> "O.OOO.",
    's'=> ".OO.O.",
    't'=> ".OOOO.",
    'u'=> "O...OO",
    'v'=> "O.O.OO",
    'w'=> ".OOO.O",
    'x'=> "OO..OO",
    'y'=> "OO.OOO",
    'z'=> "O..OOO"
}

NUM_TO_BR_DICT = {
    '1'=> "O.....",
    '2'=> "O.O...",
    '3'=> "OO....",
    '4'=> "OO.O..",
    '5'=> "O..O..",
    '6'=> "OOO...",
    '7'=> "OOOO..",
    '8'=> "O.OO..",
    '9'=> ".OO...",
    '0'=> ".OOO.."
}

BR_TO_LETTER_DICT = LETTER_TO_BR_DICT.invert
BR_TO_NUM_DICT = NUM_TO_BR_DICT.invert

def translate_braille_to_letter(arg)
    text = ""
    num_counter = 0
    cap_counter = 0
    (0...arg.length).step(6).each do |i|
      unit = arg[i, 6]
      if BR_TO_NUM_DICT.key?(unit) && num_counter > 0
        text += BR_TO_NUM_DICT[unit]
      elsif BR_TO_LETTER_DICT.key?(unit)
        if cap_counter > 0
          text += BR_TO_LETTER_DICT[unit].upcase
          cap_counter = 0
        else
          text += BR_TO_LETTER_DICT[unit]
        end
      elsif unit == CAPITAL_FOLLOWS
        cap_counter = 1
      elsif unit == NUM_FOLLOWS
        num_counter = 1
      elsif unit == SPACE
        text += ' '
        num_counter = 0 if num_counter > 0
      else
        raise "Invalid Braille character '#{unit}'."
      end
    end
    text
  end
  
  def translate_letters_to_braille(args)
    br = ""
    num_counter = 0
  
    args.each do |elem|
      elem.each_char do |i|
        if LETTER_TO_BR_DICT.key?(i)
          br += LETTER_TO_BR_DICT[i]
        elsif i == i.upcase && LETTER_TO_BR_DICT.key?(i.downcase)
          br += CAPITAL_FOLLOWS + LETTER_TO_BR_DICT[i.downcase]
        elsif NUM_TO_BR_DICT.key?(i)
          if num_counter == 0
            br += NUM_FOLLOWS + NUM_TO_BR_DICT[i]
            num_counter = 1
          else
            br += NUM_TO_BR_DICT[i]
          end
        else
          raise "Invalid character '#{i}'."
        end
      end
      br += SPACE
      num_counter = 0
    end
  
    # Cut off the last SPACE
    br = br[0...-6]
    br
  end
  
res = ""
if ARGV.length > 0
    # Edge case: if input text consists only of dots, it's considered braille
    if ARGV.length == 1 && ARGV[0].include?(".")
    res = translate_braille_to_letter(ARGV[0])
    else
    res = translate_letters_to_braille(ARGV)
    end
end
puts res