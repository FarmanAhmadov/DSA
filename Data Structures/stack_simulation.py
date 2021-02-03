class Stack:
    def __init__(self,stack = None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def __repr__(self):
        return str(self.stack)

    def push(self,value):

        self.stack.append(value)
        return self.stack

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError as e:
            return e

    def isFull(self):
        if len(self.stack) > 0:
            return True
        return False

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
        
    