class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.value
        
    def addAtHead(self, val: int) -> None:
        pred, succ = self.head, self.head.next
        self.size += 1
        to_add = ListNode(val, prev=pred, next=succ)
        pred.next = to_add
        succ.prev = to_add
        
    def addAtTail(self, val: int) -> None:
        succ, pred = self.tail, self.tail.prev
        self.size += 1
        to_add = ListNode(val, prev=pred, next=succ)
        pred.next = to_add
        succ.prev = to_add
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        pred, succ = self.head, self.head.next
        for _ in range(index):
            pred, succ = pred.next, succ.next
        self.size += 1
        to_add = ListNode(val, prev=pred, next=succ)
        pred.next = to_add
        succ.prev = to_add
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pred, succ = self.head, self.head.next
        for _ in range(index):
            pred, succ = pred.next, succ.next
        self.size -= 1
        pred.next = succ.next
        succ.next.prev = pred

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)