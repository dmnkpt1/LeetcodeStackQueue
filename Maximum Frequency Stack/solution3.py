class FreqStack(object):

    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.count:
            self.count[val] += 1
        else:
            self.count[val] = 1
        current_freq = self.count[val]

        if current_freq > self.max_freq:
            self.max_freq = current_freq
        
        if current_freq not in self.stacks:
            self.stacks[current_freq] = []
        self.stacks[current_freq].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.stacks[self.max_freq].pop()
        
        self.count[val] -= 1
        
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1
        
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()