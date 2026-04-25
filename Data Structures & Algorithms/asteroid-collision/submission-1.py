class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if (diff := a + stack[-1]) < 0:
                    stack.pop()
                else:
                    if not diff:
                        stack.pop()
                    a = 0

            if a:
                stack.append(a)

        return stack