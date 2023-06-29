class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l = len(words)-1
        for i in range(int(len(words)/2)):
            temp = words[i]
            words[i] = words[l-i]
            words[l-i] = temp

        return ' '.join(words)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords('the sky is blue'))
    print(s.reverseWords('  hello world!  '))