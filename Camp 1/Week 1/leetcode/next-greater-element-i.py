class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dict = defaultdict(lambda: -1)

        for n2 in nums2:
            while stack and n2 > stack[-1]:
                dict[stack[-1]] = n2
                stack.pop()
            
            stack.append(n2)
        ans = [0]*len(nums1)
        for i,n1 in enumerate(nums1):
            
            ans[i] = dict[n1]
            
            
        return ans