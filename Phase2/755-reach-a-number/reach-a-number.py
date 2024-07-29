class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        _sum = 0

        while True:
            if (_sum >= target) and (_sum - target) % 2 == 0:
                return k
            k += 1
            _sum += k
    