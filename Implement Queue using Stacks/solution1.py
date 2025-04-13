class MyQueue(object):

    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first_stack.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        if self.second_stack.empty():
            while self.stack_in:
                self.second_stack.append(self.first_stack.pop())

        return self.second_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.second_stack.empty():
            while self.stack_in:
                self.second_stack.append(self.first_stack.pop())

        return self.second_stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first_stack) == 0 and len(self.second_stack) == 0
