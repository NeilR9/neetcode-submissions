import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        revS = s.replace(" ", "")
        clean_S = re.sub(r"[^a-zA-z0-9]", "", revS)
        clean_S = clean_S.lower()
        print(clean_S)
        leftP = 0
        rightP = len(clean_S) - 1
        while leftP < rightP:
            if clean_S[leftP] != clean_S[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True
        