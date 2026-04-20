class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_i = stack.pop()[1]
                res[stack_i] = i - stack_i

            stack.append((t, i))

        return res