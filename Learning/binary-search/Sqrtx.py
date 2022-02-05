

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left < right:
            print("initial right", right)
            mid = (left + right + 1) // 2
            print("mid", mid)
            if mid * mid > x:
                right = mid - 1
                print("right", right)
            else:
                left = mid
                print("left", left)
        return left                
        
        
        
print(Solution.mySqrt(0, 64))       