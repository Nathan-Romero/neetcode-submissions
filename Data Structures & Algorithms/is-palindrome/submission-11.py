from string import punctuation, whitespace

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = s.translate(str.maketrans('', '', punctuation + whitespace)).lower()
        return cleaned_s == ''.join(reversed(cleaned_s))