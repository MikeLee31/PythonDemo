class Solution:
    def romanToInt(self, s: str) -> int:
        # 暴力匹配 QAQ
        num = 0
        # "MCMXCIV"
        index900 = s.find("CM")
        if index900 != -1:
            num = num + 900
            s = s[0:index900] + s[index900 + 2:]

        print(s)

        index400 = s.find("CD")
        if index400 != -1:
            num = num + 400
            s = s[0:index400] + s[index400 + 2:]
        print(s)
        index90 = s.find("XC")
        if index90 != -1:
            num = num + 90
            s = s[0:index90] + s[index90 + 2:]
        print(s)
        index40 = s.find("XL")
        if index40 != -1:
            num = num + 40
            s = s[0:index40] + s[index40 + 2:]
        print(s)
        index9 = s.find("IX")
        if index9 != -1:
            num = num + 9
            s = s[0:index9] + s[index9 + 2:]
        print(s)
        index4 = s.find("IV")
        if index4 != -1:
            num = num + 4
            s = s[0:index4] + s[index4 + 2:]
        print(s)
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in s:
            num = num + dict[i]

        print(s)
        print(num)
        return num


if __name__ == '__main__':
    Solution.romanToInt(123, "MCMXCIV")
