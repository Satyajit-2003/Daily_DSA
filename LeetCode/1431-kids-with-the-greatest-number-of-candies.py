from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ma = max(candies)
        re_arr = []
        for i in candies:
            if i + extraCandies >= ma:
                re_arr.append(True)
            else:
                re_arr.append(False)

        return re_arr

if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3], 3))
    print(s.kidsWithCandies([4,2,1,1,2], 1))