class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        stack, res = ["JFK"], []
        while stack:
            stack.append(adj[stack[-1]].pop()) if adj[stack[-1]] else res.append(stack.pop())

        return res[::-1]