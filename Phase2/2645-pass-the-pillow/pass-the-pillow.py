class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        number_of_rounds = time // (n - 1)
        number_of_hoops = time % (n - 1)

        if number_of_rounds % 2 == 1:
            return n - number_of_hoops
        else:
            return 1 + number_of_hoops
