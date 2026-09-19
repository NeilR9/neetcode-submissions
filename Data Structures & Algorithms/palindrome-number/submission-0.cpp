#include <stdio.h>
#include <string.h>
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) {
            return false;
        }
        char numStr[20];
        snprintf(numStr, sizeof(numStr), "%d", x);
        int left = 0;
        int right = strlen(numStr) - 1;
        while (left < right) {
            if (numStr[left] != numStr[right]) {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;

    }
};