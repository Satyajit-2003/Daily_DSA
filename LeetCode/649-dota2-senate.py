class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radi = []
        dire = []
        for i,s  in enumerate(senate):
            if s == 'R':
                radi.append(i)
            else:
                dire.append(i)
        ls = len(senate)

        while radi and dire:
            if radi[0] > dire[0]:
                radi.pop(0)
                dire.append(dire.pop(0)+ls)
            else:
                dire.pop(0)
                radi.append(radi.pop(0)+ls)
        
        if radi:
            return 'Radiant'
        return 'Dire'
    
if __name__ == "__main__":
    s = Solution()
    print(s.predictPartyVictory("RD"))
    print(s.predictPartyVictory("RDD"))
    print(s.predictPartyVictory("DDRRR"))
    print(s.predictPartyVictory("DRDRDRDRDRDRDRDR"))