class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0, len(s)):
            #print(f"Current element: {s[i]}")
            #print(f"Stack: {stack}")
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                if s[i] == "}" and stack[len(stack) - 1] != "{" or s[i] == "]" and stack[len(stack) - 1] != "[":
                    return False
                if s[i] == ")" and stack[len(stack) - 1] != "(":
                    return False
                stack.pop()
        return len(stack) == 0
                