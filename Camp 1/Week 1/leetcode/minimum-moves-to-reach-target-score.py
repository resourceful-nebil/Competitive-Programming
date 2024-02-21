class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while target > 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target = target // 2
                    maxDoubles -= 1
                    steps +=1
                else:
                    target -= 1
                    steps +=1
            else:
                steps += target - 1
                break
        return steps
            
