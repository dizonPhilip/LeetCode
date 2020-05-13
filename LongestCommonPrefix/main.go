package main

import "strings"

func longestCommonPrefix(strs []string) string {

	if len(strs) == 0 {
		return ""
	} else if len(strs) == 1 {
		return strs[0]
	}

	// strings.Builder is faster than making prefix a string
	// and prefix += string(char)
	prefix := strings.Builder{}
	for i := 0; i < len(strs[0]); i++ {
		matchFound := true
		char := strs[0][i]
		for j := 1; j < len(strs); j++ {
			if i >= len(strs[j]) || char != strs[j][i] {
				matchFound = false
				break
			}
		}
		if !matchFound {
			break
		}
		prefix.WriteByte(char)
	}
	return prefix.String()
}

func main() {}
