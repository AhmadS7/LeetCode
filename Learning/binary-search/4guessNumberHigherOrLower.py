class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while True:
            mid = (left+right) // 2
            current = guess(mid)
            if current > 0:
                left = mid + 1
            elif current < 0:
                right = mid - 1
            else:
                return mid
