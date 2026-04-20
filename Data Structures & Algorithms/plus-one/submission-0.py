class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = ''.join([str(d) for d in digits])
        num = int(digits) + 1
        return [int(d) for d in str(num)]