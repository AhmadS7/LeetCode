/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {

        int left = 0, right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int result = guess(mid);
            if (result == 0) {
                return mid;
            }
            else if (result < 0) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        };
        return -1;
    };
};



class Solution1 {
public:
    int guessNumber(int n) {
        for (int i = 0; i < n; i++) {
            if (guess(i) == 0) {
                return i;
            }
            return n;
        };
    };
};