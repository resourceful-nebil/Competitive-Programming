class OrderedStream:

    def __init__(self, n: int):
        # instantiates this variables to continue from where they were 
        self.arr = [""]*n
        self.ptr = 0


    def insert(self, idKey: int, value: str) -> List[str]:
        # begins from 0 index
        self.arr[idKey - 1] = value
        current_list = []

        # checks if ptr doesn't go beyond the range and if the list is empty  @ptr 
        while self.ptr < len(self.arr) and self.arr[self.ptr] != "" :
            current_list.append(self.arr[self.ptr])
            self.ptr +=1

        return current_list


         


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)