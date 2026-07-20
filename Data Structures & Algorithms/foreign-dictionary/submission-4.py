class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}
        for a, b in pairwise(words):
            if a.startswith(b) and a != b:
                return ""
            for a, b in zip(a, b):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indeg[b] += 1
                    break

        q, res = deque([c for c, d in indeg.items() if not d]), []
        while q:
            res.append(c := q.popleft())
            for nei in adj[c]:
                indeg[nei] -= 1
                if not indeg[nei]:
                    q.append(nei)

        return "" if len(res) != len(adj) else "".join(res)