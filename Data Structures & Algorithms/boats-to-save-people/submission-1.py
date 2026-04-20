class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        mx = max(people)
        count = [0] * (mx + 1)
        j = l = res = 0
        i = 1
        r = len(people) - 1

        for p in people:
            count[p] += 1

        while j < len(people):
            while not count[i]:
                i += 1

            people[j] = i
            count[i] -= 1
            j += 1

        while l <= r:
            diff = limit - people[r]
            r -= 1
            res += 1

            if l <= r and diff >= people[l]:
                l += 1

        return res