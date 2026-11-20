class Solution:
    def intToRoman(self, num: int) -> str:
        placeHolder = 1
        while num/(placeHolder * 10) > 1:
            placeHolder = placeHolder * 10
        countOff = {1 : 'I', 4 : 'IV', 5: 'V', 9: 'IX', 10: 'X', 40 :'XL', 50: 'L', 90: 'XC', 100: 'C', 400 : 'CD', 500: 'D', 900 : 'CM', 1000: 'M'}
        result = ""
        while placeHolder >= 1:
            revNum = (int(num / placeHolder)) * placeHolder
            subStr =  []
            while revNum > 0:
                if countOff.get(revNum, "Not Found") != "Not Found":
                    subStr.append(countOff[revNum])
                    revNum = 0
                else:
                    subStr.append(countOff[placeHolder])
                    revNum = revNum - placeHolder
            result += ''.join(subStr[::-1])
            num = num % placeHolder
            placeHolder = placeHolder / 10
        return result
