class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        suc = []
        
        for i in spells:
            l, r = 0, len(potions)-1

            res = len(potions)
            while l <= r:
                m = (l + r)//2
                if i * potions[m] >= success:
                    r = m - 1
                    res = m
                else:
                    l = m + 1

            suc.append(len(potions) - res)
        
        return suc

