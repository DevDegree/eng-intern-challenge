#!/usr/bin/env ruby

# Braille to English Translator
# Author: Abror Kamalov
# Date: September 11, 2024

class BrailleTranslator
    BRAILLE_TO_CHAR = {
      'O.....' => 'a', 'O.O...' => 'b', 'OO....' => 'c', 'OO.O..' => 'd', 'O..O..' => 'e',
      'OOO...' => 'f', 'OOOO..' => 'g', 'O.OO..' => 'h', '.OO...' => 'i', '.OOO..' => 'j',
      'O...O.' => 'k', 'O.O.O.' => 'l', 'OO..O.' => 'm', 'OO.OO.' => 'n', 'O..OO.' => 'o',
      'OOO.O.' => 'p', 'OOOOO.' => 'q', 'O.OOO.' => 'r', '.OO.O.' => 's', '.OOOO.' => 't',
      'O...OO' => 'u', 'O.O.OO' => 'v', '.OOO.O' => 'w', 'OO..OO' => 'x', 'OO.OOO' => 'y',
      'O..OOO' => 'z', '..OOOO' => 'number', '.....O' => 'capital'
    }.freeze
  
    CHAR_TO_BRAILLE = BRAILLE_TO_CHAR.invert.freeze
  
    NUMBER_MAP = {
      'a' => '1', 'b' => '2', 'c' => '3', 'd' => '4', 'e' => '5',
      'f' => '6', 'g' => '7', 'h' => '8', 'i' => '9', 'j' => '0'
    }.freeze
  
    def initialize(input)
      @input = input
    end
  
    def translate
      is_braille? ? braille_to_text : text_to_braille
    end
  
    private
  
    def is_braille?
      @input.match?(/\A[O.]+\z/)
    end
  
    def braille_to_text
      chars = @input.scan(/.{6}/)
      result = []
      capitalize_next = false
      number_mode = false
  
      chars.each do |char|
        case char
        when CHAR_TO_BRAILLE['capital']
          capitalize_next = true
        when CHAR_TO_BRAILLE['number']
          number_mode = true
        when ' ' * 6
          result << ' '
          number_mode = false
        else
          letter = BRAILLE_TO_CHAR[char]
          letter = NUMBER_MAP[letter] if number_mode && NUMBER_MAP.key?(letter)
          letter.upcase! if capitalize_next
          result << letter
          capitalize_next = false
        end
      end
  
      result.join
    end
  
    def text_to_braille
      result = []
      number_mode = false
      @input.each_char do |char|
        if char.match?(/[A-Z]/)
          result << CHAR_TO_BRAILLE['capital']
          char.downcase!
        elsif char.match?(/\d/)
          result << CHAR_TO_BRAILLE['number'] unless number_mode
          number_mode = true
          char = ('a'.ord + char.to_i - 1).chr
        else
          number_mode = false
        end

        result << (char == ' ' ? '......' : CHAR_TO_BRAILLE[char])
      end
      result.join
    end
  end
  
  if __FILE__ == $PROGRAM_NAME
    if ARGV.empty?
      puts "Usage: ./translator.rb <text_to_translate>"
      exit 1
    end
  
    input = ARGV.join(' ')
    translator = BrailleTranslator.new(input)
    puts translator.translate
  end