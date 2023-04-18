


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 太简单了把，切片反转就可以了
        s = str(x)
        if s[::-1] == s:
            return True
        else:
            return False



if __name__ == '__main__':
    Solution.isPalindrome(123,121)
