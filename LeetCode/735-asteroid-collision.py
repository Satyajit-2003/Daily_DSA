from typing import List

class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        stack = []

        for i in ast:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] + i < 0: 
                    stack.pop()
                elif stack[-1] + i > 0: 
                    break    
                else: 
                    stack.pop()
                    break
            else:
                stack.append(i)
        return stack


    
if __name__ == "__main__":
    s = Solution()
    print(s.asteroidCollision([5, 10, -5]))
    print(s.asteroidCollision([8, -8]))
    print(s.asteroidCollision([10, 2, -5]))