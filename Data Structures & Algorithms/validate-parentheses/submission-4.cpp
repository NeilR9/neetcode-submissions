#include <stack>
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> curStack;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
                if(curStack.empty()) {
                    return false;
                }
                if ((s[i] == ')' && curStack.top() == '(') || (s[i] == '}' && curStack.top() == '{') || (s[i] == ']' && curStack.top() == '[')) {
                    curStack.pop();
                }
                else {
                    return false;
                }
                
                continue;
            }
            curStack.push(s[i]);
        }
        return curStack.empty();
    }
};
