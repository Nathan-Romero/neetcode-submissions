class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the curr DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True