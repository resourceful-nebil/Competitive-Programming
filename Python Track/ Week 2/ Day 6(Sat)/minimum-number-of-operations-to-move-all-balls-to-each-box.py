class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        arr = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and boxes[j] == '1':
                    distance = abs(i-j)
                    arr[i] += distance
        
        return arr