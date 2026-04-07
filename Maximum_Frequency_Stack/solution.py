class FreqStack:
    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1

        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.stacks:
            self.stacks[f] = []
        self.stacks[f].append(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.stacks[self.max_freq]:
            self.max_freq -= 1

        return val
