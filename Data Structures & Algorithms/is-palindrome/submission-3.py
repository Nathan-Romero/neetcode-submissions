class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize left and right pointers in string
        l, r = 0, len(s) - 1

        # loop while l is less than r, incrementing l and decrementing r in each iteration
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # if value at l is not the same as value at r, return False
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        # return True if while loop finishes without returning
        return True

    # get the ASCII value of each character
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))