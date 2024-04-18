class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        # print(count)
        for key,val in count.items():
            res.append(val)

        heapify(res)
        ans = nlargest(k,res) 
        # print(ans)
        #count = count.most_common()
        # count = sorted(count,key = count.get,reverse=True)
        final_ = []
        # for value in ans:
        #     final_ = [key for key,val in count.items() if val == value]
        for key,val in count.items():
            if val in ans:
                final_.append(key)

        return final_
        # print() 

        # for i in range(k):
            
        #     res.append(count[])
        
        # return res 



