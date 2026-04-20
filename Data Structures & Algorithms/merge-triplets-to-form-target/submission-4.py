class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i, n in enumerate(t):
                if n == target[i]:
                    valid.add(i)

        return len(valid) == 3