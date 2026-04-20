class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = set()
        res = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not nei in visit:
                    visit.add(nei)
                    dfs(nei)

        for node in range(n):
            if not node in visit:
                visit.add(node)
                dfs(node)
                res += 1
        return res