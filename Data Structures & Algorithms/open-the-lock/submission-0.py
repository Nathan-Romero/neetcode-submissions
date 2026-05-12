class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in (deadends := {*deadends}):
            return -1

        q = deque((("0000", 0),))
        visited = {"0000"}

        while q:
            current_combination, moves = q.popleft()

            if current_combination == target:
                return moves

            for i in range(4):
                for delta in -1, 1:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = f"{current_combination[:i]}{new_digit}{current_combination[i + 1 :]}"

                    if (
                        new_combination not in visited
                        and new_combination not in deadends
                    ):
                        visited.add(new_combination)
                        q.append((new_combination, moves + 1))

        return -1