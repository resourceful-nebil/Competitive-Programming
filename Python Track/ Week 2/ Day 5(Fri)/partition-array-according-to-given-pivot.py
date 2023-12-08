class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        lesser = []
        equal = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num < pivot:
                lesser.append(num)
            else:
                equal.append(num)
        
        ans = lesser + equal + greater 
        return ans 
