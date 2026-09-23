class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        std::vector<int> resultVec(2);
        while (left < right) {
            if (numbers[left] + numbers[right] > target) {
                right -= 1;
                continue;
            }
            else if(numbers[left] + numbers[right] < target) {
                left += 1;
                continue;
            }
            resultVec[0] = left + 1;
            resultVec[1] = right + 1;
            break;
        }
        return resultVec;
    }
};
