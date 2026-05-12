class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.mp = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1

        if self.freq[val] > self.max_freq:
            self.max_freq += 1

        self.mp[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.mp[self.max_freq].pop()

        if not self.mp[self.max_freq]:
            self.max_freq -= 1

        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()