class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        l = 0
        r = k-1
        max_vow = 0
        no_vowel = 0
        for ch in s[:k]:
            if ch in vowels:
                no_vowel += 1

        while r < len(s):
            if l != 0:
                if s[l-1] in vowels:
                    no_vowel -= 1
                if s[r] in vowels:
                    no_vowel += 1
            max_vow = max(max_vow, no_vowel)
            l += 1
            r += 1

        return max_vow

if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("abciiidef", 3))
    print(s.maxVowels("aeiou", 2))
    print(s.maxVowels("leetcode", 3))