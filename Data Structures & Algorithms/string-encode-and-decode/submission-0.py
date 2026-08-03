class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        encodeStr = ""
        for curStr in strs:
            revStr = str(len(curStr)) + "|" + curStr
            encodeStr += revStr
        return encodeStr
    def decode(self, s: str) -> List[str]:
        print("Reached this")
        if s == "":
            return []
        decodeList = []
        curIndex = 0
        while curIndex < len(s):
            lengthNum = ""
            while s[curIndex] != "|":
                lengthNum += s[curIndex]
                curIndex += 1
            curIndex += 1
            length = int(lengthNum)
            counter = 1
            eleStr = ""
            while counter <= length:
                eleStr += s[curIndex]
                curIndex += 1
                counter += 1
            decodeList.append(eleStr)
        return decodeList