class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj, res = defaultdict(list), []
        tickets.sort(reverse=True)
        for u, v in tickets:
            adj[u].append(v)

        def dfs(u):
            while adj[u]:
                dfs(adj[u].pop())
            res.append(u)

        dfs("JFK")
        return res[::-1]