class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattend_list = []
        check_operations = grid[0][0] % x 

        for row in grid:
            for val in row:
                if val % x != check_operations:
                    return -1
            
                flattend_list.append(val)
        
        flattend_list.sort()
        median = flattend_list[len(flattend_list) // 2]
        res = sum(abs(v - median) // x for v in flattend_list)
        return res 