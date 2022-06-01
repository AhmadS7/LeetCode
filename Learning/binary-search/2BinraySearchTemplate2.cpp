int binraySearch(vector<int>& nums, int target) {
    if (nums.size() == 0)
        return -1;

    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        // Prevent (left+right) overflow
        int mid = left + (right - left) / 2;
        if (target == nums[mid]) { return mid; }
        else if (target < nums[mid]) { right = mid - 1; }
        else { left = mid + 1; }

    }
    // End condition left > right
    return  -1;
}