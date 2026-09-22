#include <iostream>
#include <unordered_map>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map <char, int> charTrack;
        if (s.length() <= 1) {
            return s.length();
        }
        int left = 0;
        int right = 0;
        int maxCount = 0;
        int curCount = 0;
        while (right < s.length()) {
            if (charTrack.contains(s[right]) && charTrack[s[right]] == 1) {
                maxCount = max(maxCount, curCount);
                charTrack.erase(s[left]);
                left += 1;
                curCount -= 1;
                continue;
            }
            charTrack[s[right]] = 1;
            curCount += 1;
            right += 1;
        }
        return max(maxCount, curCount);
    }
};
