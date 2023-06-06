/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{

  int *result = malloc(sizeof(int) * 2);

  int start = 0;
  int end = numsSize - 1;

  while (start <= end)
  {

    int mid = (start + end) / 2;

    if (nums[mid] == target)
    {
      start = mid;
      end = mid;

      while (start > 0 && nums[start - 1] == target)
      {
        start--;
      }

      while (end < numsSize - 1 && nums[end + 1] == target)
      {
        end++;
      }

      result[0] = start;
      result[1] = end;

      break;
    }

    else if (nums[mid] > target)
    {
      end = mid - 1;
    }

    else
    {
      start = mid + 1;
    }
  }

  if (start > end)
  {
    result[0] = -1;
    result[1] = -1;
  }

  *returnSize = 2;

  return result;
}
