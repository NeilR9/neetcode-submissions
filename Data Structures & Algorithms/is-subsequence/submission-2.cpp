class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s == t || s.length() == 0) {
            return true;
        }
        if(t.length() == 0) {
            return false;
        }
        vector<char> sArr(s.length());
        for (int i= 0; i < s.length(); i++) {
            sArr[i] = s[i];
        }
        int sLen = 0;
        int tLen = 0;
        while (sLen < sArr.size() && tLen < t.length()) {
            if (t[tLen] == sArr[sLen]) {
                sLen++;
            }
            tLen++;
        }
        return sLen == sArr.size();
    }
};