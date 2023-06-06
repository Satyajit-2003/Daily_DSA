class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            charset = [0] * 26
            for ch in i:
                charset[ord(ch) - 97] += 1
            
            if tuple(charset) not in res:
                res[tuple(charset)] = [i]
            else:
                res[tuple(charset)].append(i)
        
        return res.values()