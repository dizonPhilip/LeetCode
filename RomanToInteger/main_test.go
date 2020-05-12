package main

import "testing"

func TestRomanSingleDigit(t *testing.T) {
	i := romanToInt("V")
	expectedValue := 5
	if i != expectedValue {
		t.Errorf("Expected %v, got %v\n", expectedValue, i)
	}
}

func TestRomanMoreThanOne(t *testing.T) {
	i := romanToInt("MM")
	expectedValue := 2000
	if i != expectedValue {
		t.Errorf("Expected %v, got %v\n", expectedValue, i)
	}
}

func TestRomanSubtraction(t *testing.T) {
	i := romanToInt("IX")
	expectedValue := 9
	if i != expectedValue {
		t.Errorf("Expected %v, got %v\n", expectedValue, i)
	}
}

func TestRomanYear1994(t *testing.T) {
	i := romanToInt("MCMXCIV")
	expectedValue := 1994
	if i != expectedValue {
		t.Errorf("Expected %v, got %v\n", expectedValue, i)
	}
}

func TestRomanYear3999(t *testing.T) {
	i := romanToInt("MMMCMXCIX")
	expectedValue := 3999
	if i != expectedValue {
		t.Errorf("Expected %v, got %v\n", expectedValue, i)
	}
}

func BenchmarkRomanYear3999(b *testing.B) {
	for i := 0; i < b.N; i++ {
		romanToInt("MMMCMXCIX")
	}
}
