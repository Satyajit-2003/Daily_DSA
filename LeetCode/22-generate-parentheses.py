from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res_set = []

        def generate_paren(res, open, close):
            if open == 0 and close == 0:
                res_set.append(res)
                return
            if open != 0:
                generate_paren(res + '(', open-1, close)
            if close != 0 and open < close:
                generate_paren(res + ')', open, close-1)

        generate_paren('', n, n)
        return res_set

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))