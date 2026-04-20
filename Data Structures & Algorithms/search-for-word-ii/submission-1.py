class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visit, res = set(), set()
        root = TrieNode()

        for w in words:
            root.add_word(w)

        def dfs(r, c, node, word):
            if (not (0 <= r < m and 0 <= c < n) or
                (r, c) in visit or board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                res.add(word)

            for dr, dc in dirs:
                dfs(r + dr, c + dc, node, word)

            visit.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")

        return [*res]