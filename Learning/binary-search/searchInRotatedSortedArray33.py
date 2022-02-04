class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (high+low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[low]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] == nums[mid]:
                    low += 1
                if nums[high] == nums[mid]:
                    high -= 1
        return -1            
            