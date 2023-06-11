class Solution:
    def countAndSay(self, n: int) -> str:
        def count(s: str) -> str:
            if len(s) == 1:
                return '1' + s
            else:
                i = 0
                j = 1
                res = ''
                while j < len(s):
                    if s[i] == s[j]:
                        j += 1
                    else:
                        res += str(j-i) + s[i]
                        i = j
                        j += 1
                res += str(j-i) + s[i]
                return res

        res = '1'
        for i in range(n-1):
            res = count(res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))