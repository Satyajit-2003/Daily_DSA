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