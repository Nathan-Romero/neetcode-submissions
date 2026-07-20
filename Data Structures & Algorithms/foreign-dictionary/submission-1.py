class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for w1, w2 in pairwise(words):
            if w1.startswith(w2) and w1 != w2:
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adj[c1].add(c2)
                    break

        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            if any(dfs(nei) for nei in adj[c]):
                return True
            visit[c] = False
            res.append(c)

        return "" if any(dfs(c) for c in adj) else "".join(reversed(res))