class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int middle = left + (right - left) / 2;
        while (left <= right) {
            printf("Value of middle: %d\n", nums[middle]);
            if (nums[middle] == target) {
                return middle;
            }
            else if (nums[middle] < target) {
                left = middle + 1;
            }
            else {
                right = middle - 1;
            }
            middle = left + (right - left) / 2;
        }
        return -1;
    }
};
