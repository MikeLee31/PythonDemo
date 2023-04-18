from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        print(strs)
        flag = 1
        lens = 201
        # 获得最短元素长度，防止访问越界
        for s1 in strs:
            lens = min(lens, len(s1))
        print(lens)

        # 下标依次
        for i in range(lens):
            # 全部相同则flag1，否则就失败返回
            for ss in strs:
                if ss[i] != strs[0][i]:
                    flag = 0
                    break
            # 成功加入返回数组
            if flag==1:
                s = s + strs[0][i]
            else:
                break
        print(s)
        return s


if __name__ == '__main__':
    Solution.longestCommonPrefix(12, ["flower", "flow", "flight"])
