class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ''
        i = j = 0
        while (i < len(word1) and j < len(word2)):
            ret += (word1[i]+word2[j])
            i += 1
            j += 1

        while (i < len(word1) ):
            ret += (word1[i])
            i += 1
            
        while (j < len(word2)):
            ret += (word2[j])
            j += 1

        return ret