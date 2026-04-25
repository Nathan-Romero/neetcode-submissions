class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and 0 < stack[-1] < -a:
                    stack.pop()

                if stack and stack[-1] > 0:
                    if -a == stack[-1]:
                        stack.pop()
                    elif -a > stack[-1]:
                        stack[-1] = a
                else:
                    stack.append(a)

        return stack