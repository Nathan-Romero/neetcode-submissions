class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        n = len(edges)
        adj = defaultdict(list)

        for i in range(n):
            u, v = edges[i]
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        pq = [(-1, start_node)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end_node:
                return -prob

            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))

        return 0.0