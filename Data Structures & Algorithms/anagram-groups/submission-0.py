class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams; default value is a list to avoid one edge case
        
        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) # change count to a tuple since lists cannot be keys in python, and tuples are non-mutable

        return res.values()