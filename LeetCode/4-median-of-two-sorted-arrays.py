class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_arr = nums1 + nums2
        new_arr.sort()
        l = len(new_arr)
        if l%2 == 1:
            return new_arr[int(l/2)]
        else:
            e1 = new_arr[int(l/2)]
            e2 = new_arr[int(l/2)-1]
            return (e1+e2)/2