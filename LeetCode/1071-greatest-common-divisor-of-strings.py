class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        
        if str2 == '':
            return str1
        
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
        
# Tests
cases = [ ["ABCABC", "ABC"], ["ABABAB", "ABAB"], ["LEET", "CODE"], ["ABCDEF", "ABC"], ["ABABABAB", "ABABAB"], ["ABABABAB", "ABABABAB"], ["ABABABAB", "ABABABABAB"], ["ABABABABAB", "ABABABAB"], ["ABABABABAB", "ABABABABAB"], ["ABABABABAB", "ABABABABABAB"], ["ABABABABABAB", "ABABABABAB"], ["ABABABABABAB", "ABABABABABABAB"], ["ABABABABABABAB", "ABABABABABAB"], ["ABABABABABABAB", "ABABABABABABABAB"], ["ABABABABABABABAB", "ABABABABABABAB"], ["ABABABABABABABAB", "ABABABABABABABABAB"], ["ABABABABABABABABAB", "ABABABABABABABAB"]] 
sol = Solution()
for case in cases:
    print(sol.gcdOfStrings(case[0], case[1]))