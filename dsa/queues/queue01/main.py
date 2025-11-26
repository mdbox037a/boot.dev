class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        holder = self.items[-1]
        del self.items[-1]
        return holder

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)
