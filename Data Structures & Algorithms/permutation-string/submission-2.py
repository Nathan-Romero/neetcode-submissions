class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (m := len(s1)) > (n := len(s2)):
            return False

        if (count1 := Counter(s1)) == (count2 := Counter(s2[:m])):
            return True

        for i in range(m, n):
            count2[s2[i - m]] -= 1
            count2[s2[i]] += 1

            if count1 == count2:
                return True

        return False