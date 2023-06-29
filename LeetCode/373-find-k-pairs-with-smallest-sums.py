from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i = j = 0
        pairs = []
        while k > 0:
            pairs.append([nums1[i], nums2[j]])

            if (i < len(nums1) - 1) and (j < len(nums2) - 1):
                if nums1[i+1] <= nums2[j+1]:
                    i += 1
                else:
                    j += 1

            elif (i <= len(nums1) - 1) and (j < len(nums2) - 1):
                i = 0
                j += 1

            elif (i < len(nums1) - 1) and (j <= len(nums2) - 1):
                j = 0
                i += 1

            else:
                break

            k -= 1
        
        return pairs

if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs([1,7,11], [2,4,6], 3))
    print(s.kSmallestPairs([1,2], [3], 3))
    print(s.kSmallestPairs([1,1,2], [1,2,3], 2))