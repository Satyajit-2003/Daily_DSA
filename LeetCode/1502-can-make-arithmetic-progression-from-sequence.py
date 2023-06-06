class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canMakeArithmeticProgression([3,5,1]))
    print(s.canMakeArithmeticProgression([1,2,4]))
    print(s.canMakeArithmeticProgression([1,2]))
    print(s.canMakeArithmeticProgression([1,2,3,4,5,6,7]))