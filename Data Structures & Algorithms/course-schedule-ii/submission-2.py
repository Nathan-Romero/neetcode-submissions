class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in repeat(None, numCourses)]
        indegree = [0] * numCourses

        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1

        q = deque(i for i, n in enumerate(indegree) if not n)
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if not indegree[nei]:
                    q.append(nei)

        return res if len(res) == numCourses else []