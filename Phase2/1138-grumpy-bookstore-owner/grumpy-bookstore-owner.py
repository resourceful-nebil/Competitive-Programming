class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satsfied = 0
        window, max_window = 0,0
        l = 0
        for r in range(len(customers)):
            if grumpy[r] == 0:
                satsfied += customers[r]
            else:
                window += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            max_window = max(max_window,window)

        return max_window + satsfied
        