package translations

import "fmt"

type TranslationStrategy interface {
	Translate(text string) (string, error)
}

type Translator struct {
	Strategy TranslationStrategy
}

func NewTranslator(strategy TranslationStrategy) *Translator {
	return &Translator{Strategy: strategy}
}

func (t *Translator) Translate(text string) (string, error) {
	if t.Strategy == nil {
		return "", fmt.Errorf("translation strategy not set")
	}
	return t.Strategy.Translate(text)
}
