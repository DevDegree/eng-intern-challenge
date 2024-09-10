package translations

import "fmt"

type Operator string

const (
	CapitalFollows Operator = "CAPITAL_FOLLOWS"
	DecimalFollows          = "DECIMAL_FOLLOWS"
	NumberFollows           = "NUMBER_FOLLOWS"
)

func StringToOperator(s string) (Operator, error) {
	switch s {
	case string(CapitalFollows):
		return CapitalFollows, nil
	case string(DecimalFollows):
		return DecimalFollows, nil
	case string(NumberFollows):
		return NumberFollows, nil
	default:
		return "", fmt.Errorf("invalid BrailleOperator: %s", s)
	}
}
