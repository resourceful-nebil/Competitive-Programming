class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        arr_cnt = []
        for key,val in cnt.items():
            arr_cnt.append(val)

        top = nlargest(k,arr_cnt)

        res = []
        for key,val in cnt.items():
            if val in top:
                res.append(key)
        
        return res


