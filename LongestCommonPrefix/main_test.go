package main

import "testing"

func TestLongestPrefix(t *testing.T) {
	input := []string{"flower", "flow", "flight"}
	prefix := longestCommonPrefix(input)
	expectedOutput := "fl"
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefix2(t *testing.T) {
	input := []string{"flower", "flowed", "flow"}
	prefix := longestCommonPrefix(input)
	expectedOutput := "flow"
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefix3(t *testing.T) {
	input := []string{"flow", "flowed", "flower"}
	prefix := longestCommonPrefix(input)
	expectedOutput := "flow"
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefix4(t *testing.T) {
	input := []string{"flowes", "faired", "flower"}
	prefix := longestCommonPrefix(input)
	expectedOutput := "f"
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefixOneElement(t *testing.T) {
	input := []string{"flow"}
	prefix := longestCommonPrefix(input)
	expectedOutput := "flow"
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefixEmptyList(t *testing.T) {
	var input []string
	prefix := longestCommonPrefix(input)
	expectedOutput := ""
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefixNoMatch(t *testing.T) {
	input := []string{"dog", "racecar", "car"}
	prefix := longestCommonPrefix(input)
	expectedOutput := ""
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func TestLongestPrefixNoMatch2(t *testing.T) {
	input := []string{"", "racecar", "car"}
	prefix := longestCommonPrefix(input)
	expectedOutput := ""
	if prefix != expectedOutput {
		t.Errorf("Expected %v, got %v", expectedOutput, prefix)
	}
}

func BenchmarkLongestCommonPrefix(b *testing.B) {
	for i := 0; i < b.N; i++ {
		input := []string{"flower", "flowed", "flow"}
		longestCommonPrefix(input)
	}
}

func BenchmarkLongestCommonPrefix2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		input := []string{"flower"}
		longestCommonPrefix(input)
	}
}
