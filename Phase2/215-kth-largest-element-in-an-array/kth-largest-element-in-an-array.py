class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapify(nums)

        ans = nlargest(k,nums)
        # print(ans)
        return ans[-1]