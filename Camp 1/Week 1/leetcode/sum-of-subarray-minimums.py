class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        def nextSmallest(nums: List[int], flag) -> List[int]:
            ans = [0] * len(nums)
            nums.append(-inf)
            stack = []

            for i in range(len(nums)):

                while stack and (nums[i] < nums[stack[-1]] or (flag and nums[i] == nums[stack[-1]])):

                    x = stack.pop()
                    ans[x] = i - x

                stack.append(i)
            return ans

        left = nextSmallest(arr, False)
        right = nextSmallest(arr[::-1], True)[::-1]
        

        res = 0
        for i in range(len(arr)-1):
            res += left[i] * right[i] * arr[i]

        return res % (10**9 + 7)
        


