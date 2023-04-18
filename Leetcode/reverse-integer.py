class Solution:
    def reverse(self, x: int) -> int:
        # 注意题目要求,返回数据大小有限制,超出返回0
        s = str(x)
        flag = 1
        if s[0] == "-":
            flag = -1
            s = str(abs(x))
        s = s[::-1]
        if len(s) != 1 and s[0] == '0':
            num = int(s[1:]) * flag
        else:
            num = int(s) * flag
        if num <= 2 ** 31 - 1 and num >= - 2 ** 31:
            return num
        else:
            return 0

if __name__ == '__main__':
    print(Solution.reverse("123", 1534236469))
