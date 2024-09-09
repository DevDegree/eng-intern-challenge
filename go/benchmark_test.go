package main

import "testing"

func BenchmarkEToBSolution(b *testing.B) {
	for i := 0; i < b.N; i++ {
		EnglishToBraille("Abc 123 xYz")
	}
}
func BenchmarkBToESolution(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BrailleToEnglish(".....OO.....O.O...OO...........O.OOOO.....O.O...OO..........OO..OO.....OOO.OOOO..OOO")
	}
}
