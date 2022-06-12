# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    return sorted(str1) == sorted(str2)
print(find_anagram("heart", "earth"))
print(find_anagram("bad", "dad"))