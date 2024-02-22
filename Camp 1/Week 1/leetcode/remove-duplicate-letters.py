class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = Counter(s)
        dup = set()

        for i in range(len(s)):
            
            while stack and s[i] < stack[-1] and count[stack[-1]] > 0 and s[i] not in dup:
                x = stack.pop()
                dup.remove(x)
            
            if s[i] not in dup:
                stack.append(s[i])
                dup.add(s[i])
            count[s[i]] -= 1

        return "".join(stack)



        
        

