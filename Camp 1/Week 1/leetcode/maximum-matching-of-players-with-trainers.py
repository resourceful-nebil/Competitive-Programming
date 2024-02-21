class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        p = 0
        t = 0
        pair = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                pair += 1
                p += 1
                t += 1
            else:
                p += 1
        return pair  





