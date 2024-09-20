class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nlargest(k,nums)
        # print(arr)
        return arr[-1]