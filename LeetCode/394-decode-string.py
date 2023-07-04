class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for ch in s:
            if ch == ']':
                sub = ''
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                mult = ''
                stack.pop()
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult
                stack.append(int(mult) * sub)
            else:
                stack.append(ch)
        
        return ''.join(stack)

if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))
    print(s.decodeString("2[abc]3[cd]ef"))
    print(s.decodeString("abc3[cd]xyz"))
    print(s.decodeString("100[leetcode]"))