class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curStack = []
        for i in range(0, len(tokens)):
            if tokens[i] != "+" and tokens [i] != "*" and tokens[i] != "-" and tokens[i] != "/":
                curNum = int(tokens[i])
                curStack.append(curNum)
            else:
                num2 = curStack.pop()
                num1 = curStack.pop()
                result = 0
                if tokens[i] == "+":
                    result = num1 + num2
                elif tokens[i] == "-":
                    result = num1 - num2
                elif tokens[i] == "*":
                    result = num1 * num2
                elif tokens[i] == "/":
                    result = (int)(num1 / num2)
                curStack.append(result)
        return curStack[0]