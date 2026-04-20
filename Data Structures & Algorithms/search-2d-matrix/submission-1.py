class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bot = 0, m - 1
        while top <= bot:
            row = top + (bot - top) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        row = top + (bot - top) // 2
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False


        # l, r = 0, len(matrix) - 1

        # while l <= r:
        #     m = l + (r - l) // 2
        #     x, y = 0, len(matrix[m]) - 1
        #     if target in range(matrix[m][x], matrix[m][y] + 1):
        #         while x <= y:
        #             nMid = x + (y - x) // 2
        #             if matrix[m][nMid] == target:
        #                 return True
        #             elif matrix[m][nMid] < target:
        #                 x = nMid + 1
        #             else:
        #                 y = nMid - 1
        #         return False

        #     elif matrix[m][y] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1

        # return False