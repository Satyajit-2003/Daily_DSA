class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        prefix = ''
        i = 0
        while (i < len(str1) and i < len(str2) and str1[i] == str2[i]):
            prefix += str1[i]
            i += 1
        if i == 0:
            return ''
        temp = i
        while (i < len(str1)):
            if str1[i] != prefix[i % temp]:
                return ''
            i += 1
        i = temp
        while (i < len(str2)):
            if str2[i] != prefix[i % temp]:
                return ''
            i += 1

        return prefix
        
# Tests
cases = [ ["ABCABC", "ABC"], ["ABABAB", "ABAB"], ["LEET", "CODE"], ["ABCDEF", "ABC"], ["ABABABAB", "ABABAB"], ["ABABABAB", "ABABABAB"], ["ABABABAB", "ABABABABAB"], ["ABABABABAB", "ABABABAB"], ["ABABABABAB", "ABABABABAB"], ["ABABABABAB", "ABABABABABAB"], ["ABABABABABAB", "ABABABABAB"], ["ABABABABABAB", "ABABABABABABAB"], ["ABABABABABABAB", "ABABABABABAB"], ["ABABABABABABAB", "ABABABABABABABAB"], ["ABABABABABABABAB", "ABABABABABABAB"], ["ABABABABABABABAB", "ABABABABABABABABAB"], ["ABABABABABABABABAB", "ABABABABABABABAB"]] 
sol = Solution()
for case in cases:
    print(sol.gcdOfStrings(case[0], case[1]))