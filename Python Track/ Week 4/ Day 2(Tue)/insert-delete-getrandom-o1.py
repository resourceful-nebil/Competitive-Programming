class RandomizedSet:

    def __init__(self):
       self.values = []
       self.index_to_value = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.index_to_value:
            return False
        self.index_to_value[val] = len(self.values) # to get the index in the list 
        self.values.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.index_to_value:
            return False

        # To remove element in O(1) by swapping the element to be deleted with last element and popping
        index = self.index_to_value[val]
        self.index_to_value[self.values[-1]] = index
        del self.index_to_value[val]
        self.values[index] = self.values[-1]
        self.values.pop()
        return True 


    def getRandom(self) -> int:
        rand_index = random.randint(0,len(self.values) - 1)
        return self.values[rand_index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()