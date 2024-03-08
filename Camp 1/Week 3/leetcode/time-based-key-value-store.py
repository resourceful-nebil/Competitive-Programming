class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value = self.store[key]

        l, r = 0, len(value) - 1
        while l <= r:
            mid = (l+r)//2

            if value[mid][1] <= timestamp:
                res = value[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)