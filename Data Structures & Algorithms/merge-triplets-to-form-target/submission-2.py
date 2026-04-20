class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target

        x, y, z = target

        for i in range(len(triplets)):
            ai, bi, ci = triplets[i]

            for j in range(i + 1, len(triplets)):
                aj, bj, cj = triplets[j]

                if max(ai, aj) <= x and max(bi, bj) <= y and max(ci, cj) <= z:
                    triplets[j] = [max(ai, aj), max(bi, bj), max(ci, cj)]

                if triplets[j] == target:
                    return True

        return False