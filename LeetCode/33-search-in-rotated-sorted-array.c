int search(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize - 1;
    int mid;
    while (l <= r){
        mid = (l + r)/2;
        if (nums[mid] == target){
            return mid;
        } else if (nums[l] <= nums[mid]){
            if (target < nums[l] || target > nums[mid]){
                l = mid + 1;
            }else{
                r = mid -1;
            }
        } else{
            if (target > nums[r] || target < nums[mid]){
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
    }
    return -1;
}