#include <stack>
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> curStack;
        std::cout << "Stack Length: " << curStack.size() << "\n";
        for (int i = 0; i < s.length(); i++) {
            printf("Element: %c\n", s[i]);
            if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
                printf("Possible removal\n");
                if(curStack.empty()) {
                    return false;
                }
                if ((s[i] == ')' && curStack.top() == '(') || (s[i] == '}' && curStack.top() == '{') || (s[i] == ']' && curStack.top() == '[')) {
                    printf("yes it is!");
                    curStack.pop();
                }
                else {
                    return false;
                }
                
                continue;
            }
            curStack.push(s[i]);
        }
        std::cout << "Stack Length: " << curStack.size() << "\n";
        return curStack.empty();
    }
};
