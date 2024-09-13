package dictionary

type Dictionary struct {
	Alphabet  map[string]string
	Numbers   map[string]string
	Symbols   map[string]string
	Modifiers map[string]string
}

func NewDictionary() Dictionary {
	return Dictionary{
		Alphabet:  map[string]string{},
		Numbers:   map[string]string{},
		Symbols:   map[string]string{},
		Modifiers: map[string]string{},
	}
}

func (d *Dictionary) Reverse() Dictionary {
	return Dictionary{
		Alphabet:  reverseMap(d.Alphabet),
		Numbers:   reverseMap(d.Numbers),
		Symbols:   reverseMap(d.Symbols),
		Modifiers: reverseMap(d.Modifiers),
	}
}

func reverseMap(m map[string]string) map[string]string {
	output := make(map[string]string)
	for k, v := range m {
		output[v] = k
	}
	return output
}
