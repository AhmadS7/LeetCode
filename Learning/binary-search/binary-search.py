class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Inializing two pointers
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            #the guy
            pivot = left + (right - left)
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1      
      
      
      