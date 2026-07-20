class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        root, rank = [*range(n)], [0] * n

        def find(node):
            while root[node] != node:
                root[node] = node = root[root[node]]
            return node

        def union(u, v):
            if rank[u] < rank[v]:
                u, v = v, u
            elif rank[u] == rank[v]:
                rank[u] += 1
            root[v] = u

        for u, v in edges:
            if (u := find(u)) == (v := find(v)):
                return False
            union(u, v)

        return True