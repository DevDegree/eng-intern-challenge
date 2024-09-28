class BrailleTranslator
  def initialize
    @lexicon = {}
    @number_lexicon = {}
    add_to_lexicon(@lexicon, 'a', 'O.....')
    add_to_lexicon(@lexicon, 'b', 'O.O...')
    add_to_lexicon(@lexicon, 'c', 'OO....')
    add_to_lexicon(@lexicon, 'd', 'OO.O..')
    add_to_lexicon(@lexicon, 'e', 'O..O..')
    add_to_lexicon(@lexicon, 'f', 'OOO...')
    add_to_lexicon(@lexicon, 'g', 'OOOO..')
    add_to_lexicon(@lexicon, 'h', 'O.OO..')
    add_to_lexicon(@lexicon, 'i', '.OO...')
    add_to_lexicon(@lexicon, 'j', '.OOO..')
    add_to_lexicon(@lexicon, 'k', 'O...O.')
    add_to_lexicon(@lexicon, 'l', 'O.O.O.')
    add_to_lexicon(@lexicon, 'm', 'OO..O.')
    add_to_lexicon(@lexicon, 'n', 'OO.OO.')
    add_to_lexicon(@lexicon, 'o', 'O..OO.')
    add_to_lexicon(@lexicon, 'p', 'OOO.O.')
    add_to_lexicon(@lexicon, 'q', 'OOOOO.')
    add_to_lexicon(@lexicon, 'r', 'O.OOO.')
    add_to_lexicon(@lexicon, 's', '.OO.O.')
    add_to_lexicon(@lexicon, 't', '.OOOO.')
    add_to_lexicon(@lexicon, 'u', 'O...OO')
    add_to_lexicon(@lexicon, 'v', 'O.O.OO')
    add_to_lexicon(@lexicon, 'w', '.OOO.O')
    add_to_lexicon(@lexicon, 'x', 'OO..OO')
    add_to_lexicon(@lexicon, 'y', 'OO.OOO')
    add_to_lexicon(@lexicon, 'z', 'O..OOO')
    add_to_lexicon(@lexicon, 'cf', '.....O')
    add_to_lexicon(@lexicon, 'nf', '.O.OOO')
    add_to_lexicon(@lexicon, ' ', '......')
    add_to_lexicon(@number_lexicon, '1', 'O.....')
    add_to_lexicon(@number_lexicon, '2', 'O.O...')
    add_to_lexicon(@number_lexicon, '3', 'OO....')
    add_to_lexicon(@number_lexicon, '4', 'OO.O..')
    add_to_lexicon(@number_lexicon, '5', 'O..O..')
    add_to_lexicon(@number_lexicon, '6', 'OOO...')
    add_to_lexicon(@number_lexicon, '7', 'OOOO..')
    add_to_lexicon(@number_lexicon, '8', 'O.OO..')
    add_to_lexicon(@number_lexicon, '9', '.OO...')
    add_to_lexicon(@number_lexicon, '0', '.OOO..')
  end

  def translate(input_sentence)
    return braille_to_english input_sentence if braille? input_sentence

    english_to_braille input_sentence
  end

  private

  def braille_to_english(braille_sentence)
    braille_characters = braille_sentence.scan(/.{1,6}/)
    english_sentence = ''
    number_flag = false
    capital_flag = false

    braille_characters.each do |braille_character|
      result = @lexicon[braille_character]

      if result == 'cf'
        capital_flag = true
        next
      elsif result == 'nf'
        number_flag = true
        next
      end

      if capital_flag
        english_sentence += result.upcase
        capital_flag = false
        next
      end

      if number_flag
        if result == ' '
          number_flag = false
          english_sentence += result
          next
        else
          result = @number_lexicon[braille_character]
        end
      end

      english_sentence += result
    end

    english_sentence
  end

  def english_to_braille(english_sentence)
    braille_sentence = ''
    number_flag = false

    english_sentence.each_char do |english_character|
      case english_character
      when /[[:digit:]]/
        unless number_flag
          braille_sentence += @lexicon['nf']
          number_flag = true
        end
        braille_sentence += @number_lexicon[english_character]
        next
      when ' '
        number_flag = false
      when english_character.upcase
        english_character = english_character.downcase
        braille_sentence += @lexicon['cf']
      end
      braille_sentence += @lexicon[english_character]
    end

    braille_sentence
  end

  def add_to_lexicon(set, english_char, braille_char)
    set[english_char] = braille_char
    set[braille_char] = english_char
  end

  def braille?(str)
    str.count('^O.').zero?
  end
end

braille_translator = BrailleTranslator.new
input = ARGV.join ' '
print braille_translator.translate input
