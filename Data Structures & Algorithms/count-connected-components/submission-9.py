class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root, rank = [*range(n)], [0] * n

        def find(node):
            while root[node] != node:
                root[node] = node = root[root[node]]
            return node

        def union(u, v):
            if (u := find(u)) == (v := find(v)):
                return 0

            if rank[u] < rank[v]:
                u, v = v, u
            elif rank[u] == rank[v]:
                rank[u] += 1

            root[v] = u
            return 1

        for u, v in edges:
            n -= union(u, v)

        return n