package braille

func IsBraille(s string) bool {
	for _, c := range s {
		if c != '.' && c != 'O' {
			return false
		}
	}
	return true
}

func IsCapital(s rune) bool {
	return s >= 'A' && s <= 'Z'
}

func IsNumber(s rune) bool {
	return s >= '0' && s <= '9'
}

func ToUpper(s rune) rune {
	if s >= 'a' && s <= 'z' {
		return s - 'a' + 'A'
	}
	return s
}

func ToLower(s rune) rune {
	if s >= 'A' && s <= 'Z' {
		return s - 'A' + 'a'
	}
	return s
}

func ToBraille(s string) string {
	res := ""
	for i := 0; i < len(s); i++ {
		if IsCapital(rune(s[i])) {
			// Add capital follows and output lowercase
			res += EnglishToBraille["capital"]
			res += EnglishToBraille[string(ToLower(rune(s[i])))]
		} else if IsNumber(rune(s[i])) {
			// Consume all numbers until a space
			res += EnglishToBraille["number"]
			j := i
			for ; j < len(s) && IsNumber(rune(s[j])) && s[j] != ' '; j++ {
				res += NumberToBraille[string(s[j])]
			}
			i = j - 1
		} else {
			res += EnglishToBraille[string(s[i])]
		}
	}
	return res
}

func ToEnglish(s string) string {
	res := ""
	for i := 0; i < len(s); i += 6 {
		braille := s[i : i+6]
		if BrailleToEnglish[braille] == "capital" {
			i += 6
			next_braille := s[i : i+6]
			res += string(ToUpper(rune(BrailleToEnglish[next_braille][0])))
		} else if BrailleToEnglish[braille] == "number" {
			for ; i < len(s) && BrailleToEnglish[s[i:i+6]] != " "; i += 6 {
				res += BrailleToNumber[s[i:i+6]]
			}
			i -= 6
		} else {
			res += BrailleToEnglish[braille]
		}
	}
	return res
}
