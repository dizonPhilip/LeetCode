package main

func romanToInt(s string) int {
	romanMap := map[int]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	var total int
	for i := 0; i < len(s); i++ {
		val := romanMap[int(s[i])]
		if i+1 < len(s) {
			nextVal := romanMap[int(s[i+1])]
			if val < nextVal {
				val = nextVal - val
				i++
			}
		}
		total += val
	}
	return total
}

func main() {}
