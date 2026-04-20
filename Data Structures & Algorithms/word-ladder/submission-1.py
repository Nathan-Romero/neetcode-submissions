class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adj = defaultdict(list)
        q = deque([beginWord])
        visit = {beginWord}
        res = 1

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                adj[pattern].append(word)

        while q:
            n = len(q)

            for _ in range(n):
                word = q.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]

                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            res += 1

        return 0