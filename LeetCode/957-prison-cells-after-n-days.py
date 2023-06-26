from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        memo = []
        def next_day(cells: List[int]) -> List[int]:
            next_cells = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    next_cells[i] = 1
            return next_cells
        
        # while n > 0:
        #     temp = next_day(cells)
        #     if (len(memo) > 0 and memo[0][0] == temp):
        #         print("Is this working?")
        #         return memo[n % len(memo)][1]
        #     memo.append((cells, temp))
        #     cells = temp
        #     n -= 1

        for i in range(n%14 + 14):
            cells = next_day(cells)

        return cells

if __name__ == "__main__":
    s = Solution()
    print(s.prisonAfterNDays([0,1,0,1,1,0,0,1], 7))
    print(s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000))