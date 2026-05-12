class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        res = []

        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def dfs(x, y, visit):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            for i in graph[x]:
                if i not in visit:
                    visit.add(i)
                    temp = dfs(i, y, visit)

                    if temp != -1:
                        return graph[x][i] * temp

            return -1

        for x, y in queries:
            res.append(dfs(x, y, set()))

        return res