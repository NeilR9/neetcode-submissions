class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        hashArray = []
        hashMap = {}
        hashArray.append([strs[0]])
        hashMap[''.join(sorted(strs[0]))] = 0
        curIndex = 1
        for curWord in strs[1:]:
            revWord = ''.join(sorted(curWord))
            if hashMap.get(revWord, "No Word") != "No Word":
                hashArray[hashMap[revWord]].append(curWord)
            else:
                hashArray.append([curWord])
                hashMap[''.join(sorted(curWord))] = curIndex
                curIndex += 1
        return hashArray

         
        
        