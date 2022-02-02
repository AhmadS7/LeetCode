class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hashMap = {}
            
            for i,n in enumerate(nums):
                maybe = target - nums[i]
                if maybe in hashMap:
                    return [hashMap[maybe], i]
                hashMap[n] = i
            return     