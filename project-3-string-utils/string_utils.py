def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(reverse_words("Hello World"))
print(count_vowels("I am a strong man."))
print(is_palindrome("abcdcba"))
