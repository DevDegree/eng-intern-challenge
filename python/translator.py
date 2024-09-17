def main(input):
	print(input)
	if isBraille(input):
		brailleStrings = splitBraille(input)

def isBraille(input):
	for c in input:
		if (c != '.' and c != 'O'):
			return False
	return True

def splitBraille(input):
	return splitBrailleTail(input, [])


def splitBrailleTail(input, output):
	if len(input) == 0:
		return output
	else:
		output.append(input[0:6])
		return splitBrailleTail(input[6:], output)

main(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")


