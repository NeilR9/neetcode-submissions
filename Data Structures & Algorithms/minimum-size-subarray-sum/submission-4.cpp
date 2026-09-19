class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if (nums.size() == 1) {
            if (nums[0] == target) {
                return 1;
            }
            return 0;
        }
        int left = 0;
        int right = 0;
        int minLength = nums.size() + 1;
        int curSum = nums[left];
        while (right < nums.size()) {
            //printf("Left Value: %d\n", left);
            //printf("Right Value: %d\n", right);
            if  (curSum >= target) {
                //printf("Found length: %d\n", right - left + 1);
                //printf("Current min length: %d\n", minLength);
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    //printf("New min length: %d\n", minLength);
                }
                curSum -= nums[left];
                left += 1;
            }
            else {
                right += 1;
                if (right < nums.size()) {  
                    curSum += nums[right];
                }
            }
        } 
        if (minLength == nums.size() + 1) {
            return 0;
        }
        return minLength;
    }
};