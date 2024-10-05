class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = set()
        unlocked = [False for _ in range(len(rooms))]
        unlocked[0] = True


        while q:
            for _ in range(len(q)):
                tmp = q.popleft()
                for key in rooms[tmp]:
                    unlocked[key] = True
                    if key not in visited:
                        q.append(key)
                    visited.add(key)

        # print(unlocked)
        return all(unlocked)
                
                    


