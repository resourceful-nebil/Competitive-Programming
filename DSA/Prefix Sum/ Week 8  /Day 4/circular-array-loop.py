class Solution:

    def getNextIndex(self,nums:List[int], i:int) -> int:
        n = len(nums)
        return (i + nums[i]) % n
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = self.getNextIndex(nums, i)

            while nums[fast] * nums[i] > 0 and nums[self.getNextIndex(nums, fast)] * nums[i] > 0:
                if slow == fast:
                    if slow == self.getNextIndex(nums, slow):
                        break
                    return True

                slow = self.getNextIndex(nums, slow)
                fast = self.getNextIndex(nums, self.getNextIndex(nums, fast))

            # Mark the current loop as visited
            j = i
            while nums[j] * nums[i] > 0:
                nextIndex = self.getNextIndex(nums, j)
                nums[j] = 0
                j = nextIndex

        return False

    