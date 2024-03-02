class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        R,D = deque(),deque()

        # to construct the queue using the indexes
        for i,c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        
        # deciding which one to pop
        while D and R:
            rturn = R.popleft()
            dturn = D.popleft()
        
            if rturn > dturn:
                D.append(rturn + len(senate))
            else:
                R.append(rturn + len(senate))

        return "Dire" if D else "Radiant"


        
        