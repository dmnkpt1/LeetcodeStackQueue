class MyStack(object):

    def __init__(self):
        self.first_queue = []
        self.second_queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.second_queue.append(x)
        while self.first_queue:
            self.second_queue.append(self.first_queue.pop(0))
        self.first_queue = self.second_queue
        self.second_queue = []


    def pop(self):
        """
        :rtype: int
        """
        return self.first_queue.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.first_queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first_queue) == 0
