class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in repeat(None, numCourses)]
        prereq = [set() for _ in repeat(None, numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:
            adj[u].add(v)
            indegree[v] += 1

        q = deque(i for i in range(numCourses) if not indegree[i])

        while q:
            for nei in adj[node := q.popleft()]:
                prereq[nei].add(node)
                prereq[nei] |= prereq[node]
                indegree[nei] -= 1

                if not indegree[nei]:
                    q.append(nei)

        return [u in prereq[v] for u, v in queries]