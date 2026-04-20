class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = res = 0
        r = len(people) - 1

        while l <= r:
            diff = limit - people[r]
            r -= 1
            res += 1

            if l <= r and diff >= people[l]:
                l += 1

        return res