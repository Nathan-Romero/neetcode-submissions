class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned_s == ''.join(reversed(cleaned_s))