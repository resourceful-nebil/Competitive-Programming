from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.topElement = 0

    def push(self, x):
        self.q1.put(x)
        self.topElement = x

    def pop(self):
        while self.q1.qsize() > 1:
            self.topElement = self.q1.queue[0]
            self.q2.put(self.topElement)
            self.q1.get()

        poppedElement = self.q1.queue[0]
        self.q1.get()

        self.q1, self.q2 = self.q2, self.q1
        return poppedElement

    def top(self):
        return self.topElement

    def empty(self):
        return self.q1.empty()