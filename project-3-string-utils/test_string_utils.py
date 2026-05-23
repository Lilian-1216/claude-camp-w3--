# test_string_utils.py
from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words_normal():
    assert reverse_words("good night") == "night good"

def test_reverse_words_single():
    assert reverse_words("bingo") == "bingo"

def test_reverse_words_empty():
    assert reverse_words("") == ""

def test_count_vowels_normal():
    assert count_vowels("good night") == 3

def test_count_vowels_empty():
    assert count_vowels("") == 0

def test_count_vowels_no_vowels():
    assert count_vowels("rhythm") == 0

def test_count_vowels_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_count_vowels_mixed_case():
    assert count_vowels("GOOd NIGHT") == 3

def test_is_palindrome_true():
    assert is_palindrome("abcdcba") == True

def test_is_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_empty():
    assert is_palindrome("") == True

def test_is_palindrome_single_char():
    assert is_palindrome("a") == True

def test_is_palindrome_mixed_case():
    assert is_palindrome("Aba") == True

