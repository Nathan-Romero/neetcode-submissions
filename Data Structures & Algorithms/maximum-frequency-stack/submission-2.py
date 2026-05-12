from heapq import heappush_max, heappop_max

class FreqStack:
    def __init__(self):
        self.max_heap = []
        self.freq = defaultdict(int)
        self.i = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heappush_max(self.max_heap, (self.freq[val], self.i, val))
        self.i += 1

    def pop(self) -> int:
        self.freq[val := heappop_max(self.max_heap)[2]] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()