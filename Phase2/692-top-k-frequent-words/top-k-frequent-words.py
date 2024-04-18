class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        sotred_ = sorted(count,key = lambda x: (-count[x],x))
        print(sotred_)

        heap = [val for key,val in count.items()]

        heapify(heap)
        ans = nlargest(k,heap)

        # final_ = [key for key,val in sotred_.items() if val in ans]
        # final_ = nlargest(k,)

        
        return sotred_[:k]
