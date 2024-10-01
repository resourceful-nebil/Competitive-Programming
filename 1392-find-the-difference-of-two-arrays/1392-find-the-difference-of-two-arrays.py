class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans = [[],[]]
        for n in nums1:
            if n not in nums2:
                ans[0].append(n)
        
        for n in nums2:
            if n not in nums1:
                ans[1].append(n)
        
        return ans
        
