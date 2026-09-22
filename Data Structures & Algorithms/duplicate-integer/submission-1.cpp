#include <iostream>
#include <unordered_map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map <int,int> freqCount;
        for (int num: nums) {
            if(freqCount.contains(num)) {
                return true;
            }
            freqCount[num] = 1;
        }
        return false;
    }

};