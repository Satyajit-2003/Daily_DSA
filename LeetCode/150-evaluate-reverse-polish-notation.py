from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch  == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 + op2)
            elif ch  == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif ch  == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 * op2)
            elif ch  == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(trunc(op1 / op2))
            else:
                stack.append(int(ch))
            print(stack, ch)

        return stack[-1]
            

if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2","1","+","3","*"])) # 9
    print(s.evalRPN(["4","13","5","/","+"])) # 6
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # 22