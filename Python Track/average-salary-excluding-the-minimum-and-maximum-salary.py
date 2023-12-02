class Solution:
    def average(self, salary: List[int]) -> float:
        maximum = max(salary)
        minimum = min(salary)
        ans= 0
        filtered = [n for n in salary if n!=maximum and n!=minimum]
        for a in filtered:
            ans += a
        size= len(filtered)
        ans = (ans/size)
        return ans
