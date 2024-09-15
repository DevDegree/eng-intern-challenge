package main

import (
  "os"
  "fmt"
  "strings"
  "unicode"
)

func getEnglishForBraille(s string) string{
  brailleToEnglish := map[string]string{
		"O.....": "a",
		"O.O...": "b",
		"OO....": "c",
		"OO.O..": "d",
		"O..O..": "e",
		"OOO...": "f",
		"OOOO..": "g",
		"O.OO..": "h",
		".OO...": "i",
		".OOO..": "j",
		"O...O.": "k",
		"O.O.O.": "l",
		"OO..O.": "m",
		"OO.OO.": "n",
		"O..OO.": "o",
		"OOO.O.": "p",
		"OOOOO.": "q",
		"O.OOO.": "r",
		".OO.O.": "s",
		".OOOO.": "t",
		"O...OO": "u",
		"O.O.OO": "v",
		".OOO.O": "w",
		"OO..OO": "x",
		"OO.OOO": "y",
		"O..OOO": "z",
		"......": " ",
	}
  return brailleToEnglish[s]
}

func getNumberForBraille(s string) string{
  brailleToNumber := map[string]string{
		"O.....": "1",
		"O.O...": "2",
		"OO....": "3",
		"OO.O..": "4",
		"O..O..": "5",
		"OOO...": "6",
		"OOOO..": "7",
		"O.OO..": "8",
		".OO...": "9",
		".OOO..": "0",
	}
  return brailleToNumber[s]
}

func isOperator(s string) (bool, string){
  switch s{
  case ".....O":
    return true, "shift"
  case ".O.OOO":
    return true, "number"
  }

  return false, ""
}

func getBrailleForEnglish(r rune) string{
  englishToBraille := map[rune]string{
		'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
		'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
		'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
		'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
		'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
		'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
		'y': "OO.OOO", 'z': "O..OOO", ' ': "......", 'S': ".....O",
		'N': ".O.OOO",
	}
  return englishToBraille[r]
}

func getBrailleForNumber(r rune) string  {
  numberToBraille := map[rune]string{
		'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
		'5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
		'9': ".OO...", '0': ".OOO..",
	}
  return numberToBraille[r]
}

func isBraille(s string) bool {
  for _, el := range s{
    if el != 46 && el != 79{
      return false
    } 
  }
  return true
}

func translateFromBrailleToEnglish(s string) string{
  tokens := make([]string, 0, len(s)/6)
  numberFlag := false
  shiftFlag := false
  for len(s) > 5{
    token := s[:6]
    s = s[6:]
    opOk, operator := isOperator(token)
    if opOk {
      switch operator{
      case "shift":
        shiftFlag = true
      case "number":
        numberFlag = true
      }
    }else{
      if numberFlag{
        tokens = append(tokens, getNumberForBraille(token))
      }else{
        letter := getEnglishForBraille(token)
        if letter == " "{
          numberFlag = false
        }else{
          if shiftFlag {
            letter = strings.ToTitle(letter)
            shiftFlag = false
          }
        }
        tokens = append(tokens, letter)
      }
    }
  }

  return strings.Join(tokens, "")
}

func translateFromEnglishToBraille(s string) string{
  numberFlag := false
  tokens := make([]string, 0, len(s))
  for _, r := range s{
    var token string
    if unicode.IsNumber(r)  {
      if !numberFlag {
        numberFlag = true
        token += ".O.OOO"
      }
      token += getBrailleForNumber(r) 
    }else if r == ' '{
      numberFlag = false
      token = "......"
    }else {
      if r == unicode.ToUpper(r){
        token += ".....O"
      }
      token += getBrailleForEnglish(unicode.ToLower(r))
    }
    tokens = append(tokens, token)
  }
  return strings.Join(tokens, "")
}

func main(){
  
  input := strings.Join(os.Args[1:], " ")
  braileToEnglish := isBraille(input)

  var result string
  if braileToEnglish {
    if len(input) % 6 != 0 {
      fmt.Println("Braille Sequence is incomplete.")
      return
    }
    result = translateFromBrailleToEnglish(input)
  }else{
    result = translateFromEnglishToBraille(input)
  }
  fmt.Print(result)
}
