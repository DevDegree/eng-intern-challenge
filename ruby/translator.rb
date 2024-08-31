#!/usr/bin/env ruby

$capital_follows_braille = '.....O'
$decimal_follows_braille = '.O...O'
$number_follows_braille = '.O.OOO'
$space_braille = '......'
$alphabet_to_braille_map = {
  'a'=> 'O.....',
  'b'=> 'O.O...',
  'c'=> 'OO....',
  'd'=> 'OO.O..',
  'e'=> 'O..O..',
  'f'=> 'OOO...',
  'g'=> 'OOOO..',
  'h'=> 'O.OO..',
  'i'=> '.OO...',
  'j'=> '.OOO..',
  'k'=> 'O...O.',
  'l'=> 'O.O.O.',
  'm'=> 'OO..O.',
  'n'=> 'OO.OO.',
  'o'=> 'O..OO.',
  'p'=> 'OOO.O.',
  'q'=> 'OOOOO.',
  'r'=> 'O.OOO.',
  's'=> '.OO.O.',
  't'=> '.OOOO.',
  'u'=> 'O...OO',
  'v'=> 'O.O.OO',
  'w'=> '.OOO.O',
  'x'=> 'OO..OO',
  'y'=> 'OO.OOO',
  'z'=> 'O..OOO',
}
$number_to_braille_map = {
  '1'=> 'O.....',
  '2'=> 'O.O...',
  '3'=> 'OO....',
  '4'=> 'OO.O..',
  '5'=> 'O..O..',
  '6'=> 'OOO...',
  '7'=> 'OOOO..',
  '8'=> 'O.OO..',
  '9'=> '.OO...',
  '0'=> '.OOO..',
}
$symbol_to_braille = {
  '.'=> '..OO.O',
  ','=> '..O...',
  '?'=> '..O.OO',
  '!'=> '..OOO.',
  '=>'=> '..OO..',
  ';'=> '..O.O.',
  '-'=> '....OO',
  '/'=> '.O..O.',
  '<'=> '.OO..O',
  '>'=> 'O..OO.',
  '('=> 'O.O..O',
  ')'=> '.O.OO.',
  ' '=> $space_braille,
}
$braille_to_alphabet_map = {
  'O.....'=> 'a',
  'O.O...'=> 'b',
  'OO....'=> 'c',
  'OO.O..'=> 'd',
  'O..O..'=> 'e',
  'OOO...'=> 'f',
  'OOOO..'=> 'g',
  'O.OO..'=> 'h',
  '.OO...'=> 'i',
  '.OOO..'=> 'j',
  'O...O.'=> 'k',
  'O.O.O.'=> 'l',
  'OO..O.'=> 'm',
  'OO.OO.'=> 'n',
  'O..OO.'=> 'o',
  'OOO.O.'=> 'p',
  'OOOOO.'=> 'q',
  'O.OOO.'=> 'r',
  '.OO.O.'=> 's',
  '.OOOO.'=> 't',
  'O...OO'=> 'u',
  'O.O.OO'=> 'v',
  '.OOO.O'=> 'w',
  'OO..OO'=> 'x',
  'OO.OOO'=> 'y',
  'O..OOO'=> 'z',
}
$braille_to_number_map = {
  'O.....'=> '1',
  'O.O...'=> '2',
  'OO....'=> '3',
  'OO.O..'=> '4',
  'O..O..'=> '5',
  'OOO...'=> '6',
  'OOOO..'=> '7',
  'O.OO..'=> '8',
  '.OO...'=> '9',
  '.OOO..'=> '0',
}
$braille_to_symbol_map = {
  '..OO.O'=> '.',
  '..O...'=> ',',
  '..O.OO'=> '?',
  '..OOO.'=> '!',
  '..OO..'=> '=>',
  '..O.O.'=> ';',
  '....OO'=> '-',
  '.O..O.'=> '/',
  '.OO..O'=> '<',
  'O..OO.'=> '>',
  'O.O..O'=> '(',
  '.O.OO.'=> ')',
  [$space_braille]=> ' ',
}

def eng_to_braille(input)
  capitalized_alphabet_regex = /^[A-Z]$/
  non_capitalized_alphabet_regex = /^[a-z]$/
  number_regex = /^[0-9]$/
  index = 0
  number_mode = false
  res = ''
  for index in 0 ... input.length
    char = input[index, 1]
    case char
    when ' '
      res += $space_braille
      number_mode = false
    when capitalized_alphabet_regex
      res += "#{$capital_follows_braille}#{$alphabet_to_braille_map[char.downcase]}"
    when non_capitalized_alphabet_regex
      res += $alphabet_to_braille_map[char]
    when number_regex
      if not number_mode
        res += "#{$number_follows_braille}#{$number_to_braille_map[char]}"
        number_mode = true
      else
        res += $number_to_braille_map[char]
      end
    when '.'
      if number_mode
        res += decimal_follows_braille
      else
        if index + 1 < input.length and number_regex.match(input[index+1, 1])
          # looks at the next char to see if this is a decimal (example: .5)
          res += "#{$number_follows_braille}#{$decimal_follows_braille}"
          number_mode = true
        else
          res += $symbol_to_braille[char]
        end
      end
    else
      res += $symbol_to_braille[char] || ''
    end
  end
  return res
end

def braille_to_eng(input)
  index = 0
  capital_index = -1
  number_mode = false
  res = ''
  while index < input.size
    braille = input[index, 6]
    case braille
    when $space_braille
      res += ' '
      number_mode = false
    when $capital_follows_braille
      capital_index = index + 6
    when $number_follows_braille
      number_mode = true
    when $decimal_follows_braille
      res += '.'
    else
      capitalize = capital_index == index
      res += braille_letter_to_eng(braille, capitalize, number_mode)
    end
    index += 6
  end
  return res
end

def braille_letter_to_eng(braille, capitalize, number_mode)
  if number_mode
    return use_symbol_for_non_map_letter(
      braille,
      $braille_to_number_map,
    )
  else
    if capitalize
      return use_symbol_for_non_map_letter(
        braille,
        $braille_to_alphabet_map,
      ).capitalize()
    else
      return use_symbol_for_non_map_letter(
        braille,
        $braille_to_alphabet_map,
      )
    end
  end
end

def use_symbol_for_non_map_letter(braille, mapping)
  if mapping.key?(braille)
    return mapping[braille]
  else
    return $braille_to_symbol_map[braille] || ''
  end
end

def braille_input(inputs)
  if ARGV.size > 1
    # braille only contains 'O' and '.', having a size > 1 means it contains whitespace
    return false
  end
  all_braille_regex = /^[.O]+$/
  for index in 0... inputs.size
    str_len = inputs[index].length
    if str_len % 6 != 0
      # each braille letter is made of a combo of 6 'O' and '.', so any valid braille input should be divisable by 6 in terms of length
      return false
    end
    if not all_braille_regex.match(inputs[index])
      # braille only has 'O' and '.', so any character aside of those two makes the input invalid
      return false
    end
  end
  return true
end

def translate(inputs)
  use_braille_to_eng_translation = braille_input(inputs)
  input = inputs.join(' ')
  if use_braille_to_eng_translation
    output = braille_to_eng(input)
  else
    output = eng_to_braille(input)
  end
  return output
end

puts translate(ARGV)
