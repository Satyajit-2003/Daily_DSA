class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1

        vowel = 'aeiou'
        arr = [i for i in s]

        while l < r:
            while l < r and arr[l].lower() not in vowel:
                l += 1
            while l < r and arr[r].lower() not in vowel:
                r -= 1
            
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp

            l += 1
            r -= 1

        return ''.join(arr)
