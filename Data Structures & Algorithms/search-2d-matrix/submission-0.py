class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + (r - l) // 2
            x, y = 0, len(matrix[m]) - 1
            if target in range(matrix[m][x], matrix[m][y] + 1):
                while x <= y:
                    nMid = x + (y - x) // 2
                    if matrix[m][nMid] == target:
                        return True
                    elif matrix[m][nMid] < target:
                        x = nMid + 1
                    else:
                        y = nMid - 1
                return False

            elif matrix[m][y] < target:
                l = m + 1
            else:
                r = m - 1

        return False