void rotate(int* nums, int numsSize, int k){
    if (numsSize == 0 || numsSize == 1){
        return ;
    }
    if (k > numsSize){
        k = k % numsSize ;
    }
    int temp;
    // Reversing the last k elements
    for(int i = 0; i < k/2; i++){
        temp = nums[numsSize - i - 1];
        nums[numsSize - i - 1] = nums[numsSize - k + i];
        nums[numsSize - k + i] = temp;
    }

    //Reversing the first n-k elements
    for (int i = 0; i < (numsSize-k)/2; i++){
        temp = nums[i];
        nums[i] = nums[numsSize-k-i-1];
        nums[numsSize-k-i-1] = temp;
    }

    //Reversing the entire array
    for (int i = 0; i < numsSize/2; i ++){
        temp = nums[i];
        nums[i] = nums[numsSize-i-1];
        nums[numsSize-i-1] = temp;
    }

}