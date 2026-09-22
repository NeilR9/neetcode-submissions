#include <string>
#include <unordered_map>
#include <algorithm>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        //better to check frequecy character count of each string
        
        std::unordered_map<char, int> freqCountsS;
        std::unordered_map<char, int> freqCountsT;
        for (int i = 0; i < s.length(); i++) {
            if(freqCountsS.contains(s[i])) {
                freqCountsS[s[i]] += 1;
                continue;
            }
            freqCountsS[s[i]] = 1;
        }
        for (int i = 0; i < t.length(); i++) {
            if(freqCountsT.contains(t[i])) {
                freqCountsT[t[i]] += 1;
                continue;
            }
            freqCountsT[t[i]] = 1;
        }
        return freqCountsS == freqCountsT;
        

    }
};
