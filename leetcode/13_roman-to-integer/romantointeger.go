package main

import (
	"fmt"
	"strings"
)

// challenge from leetcode #13 (https://leetcode.com/problems/roman-to-integer/submissions/)
func main() {
	romanNumber := "MCMXCIV"
	romansToInt := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	romanNumberSplit := strings.Split(romanNumber, "")
	romanNumberSplitLen := len(strings.Split(romanNumber, ""))
	i := 0
	for idx, val := range romanNumberSplit {
		if romanNumberSplitLen > idx+1 {
			next := romanNumberSplit[idx+1]
			if val == "I" && (next == "V" || next == "X") {
				i -= 1
				continue
			}
			if val == "X" && (next == "L" || next == "C") {
				i -= 10
				continue
			}
			if val == "C" && (next == "D" || next == "M") {
				i -= 100
				continue
			}
		}
		i += romansToInt[val]
	}
	fmt.Println(i)
}
