class Solution
{
public:
  int search(vector<int> &nums, int target)
  {
    if (nums.size() == 0) return -1;


    int left = 0, right = nums.size() - 1;

    while (left <= right)
    {
      int pivot = left + (right - left) / 2;
      if (nums[pivot] == target)
      {
        return pivot;
      }
      else if (nums[pivot] > nums[left])
      {
        if (nums[left] <= target && target < nums[pivot])
        {
          right = pivot - 1;
        }
        else
        {
          left = pivot + 1;
        }
      }
      else if (nums[pivot] < nums[right])
      {
        if (nums[pivot] < target && target <= nums[right])
        {
          left = pivot + 1;
        }
        else
        {
          right = pivot - 1;
        }
      }
      else
      {
        if (nums[left] == nums[pivot])
          left = left + 1;

        if (nums[right] == nums[pivot])
          right = right - 1;
      }
    }
    return -1;
  }
};
