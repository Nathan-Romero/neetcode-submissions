class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in repeat(None, numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)

        q = deque(i for i, n in enumerate(indegree) if not n)
        taken = 0

        while q:
            node = q.popleft()
            taken += 1

            for nei in adj[node]:
                indegree[nei] -= 1

                if not indegree[nei]:
                    q.append(nei)

        return taken == numCourses