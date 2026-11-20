class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        stringSet = set()
        left = 0
        right = 0
        lenCount = 0
        maxCount = 0
        while right < len(s):
            if s[right] not in stringSet:
                stringSet.add(s[right])
                lenCount += 1
                right += 1
                continue
            elif left < right:
                stringSet.remove(s[left])
                left += 1
                if lenCount > maxCount:
                    maxCount = lenCount
                lenCount -= 1
                continue
            else:
                right += 1
                lenCount += 1
        return max(maxCount, lenCount)
