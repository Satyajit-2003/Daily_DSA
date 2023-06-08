from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last = output[-1][1]

            if start <= last:
                output[-1][1] = max(last, end)
            else:
                output.append([start, end])

        return output

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
    print(s.merge([[1,4],[0,4]]))
    print(s.merge([[1,4],[0,0]]))