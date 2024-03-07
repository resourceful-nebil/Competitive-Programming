class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr,x)
        l, r = idx - 1, idx % len(arr)
        res = []

        while k> 0:
            a,b = arr[l], arr[r]
            if abs(a - x) <= abs(b - x):
                res.append(a)
                l -= 1 

            elif abs(a - x) > abs(b - x):
                res.append(b)
                r = (r + 1) % len(arr)
            k -= 1
            
        res.sort()
        return res