def binarySearch2(nums, target):
    """[summary]

    Args:
        nums ([type]): [description]
        target ([type]): [description]
    """
    if len(nums) == 0:
      return -1
    
    left, right = 0, len(nums)
    while left < right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = nums[mid]
      else:
        right = nums[mid]
        
    if left != len(nums) and nums[left] == target:
      return left
    return -1      
      
      
      
print(binarySearch2([1,2,3,4,5,6,7,8,9], 7))      
      