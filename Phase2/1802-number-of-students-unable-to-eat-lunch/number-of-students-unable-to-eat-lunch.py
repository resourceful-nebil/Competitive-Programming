class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        stack = sandwiches[::-1]


        while stack:
            if stack[-1] == queue[0]:
                stack.pop()
                queue.popleft()
            elif stack[-1] != queue[0] and stack[-1] in queue:
                tmp = queue.popleft()
                queue.append(tmp)
            
            elif stack[-1] != queue[0] and stack[-1] not in queue:
                return len(stack)

        
        return len(stack)