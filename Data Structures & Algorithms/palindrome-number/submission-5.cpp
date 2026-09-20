class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        if (x < 10) {
            return true;
        }
        int placeHolder = 10;
        while (x / placeHolder >= 10) {
            placeHolder *= 10;
        }
        while (x) {
            int digit = (x / placeHolder);
            int oppDigit = x % 10;
            if (digit != oppDigit) {
                return false;
            }
            x = (x % placeHolder)/10;
            placeHolder = (placeHolder / 10)/10;
        }
        return true;
    }
};