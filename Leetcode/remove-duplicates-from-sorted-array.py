from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 题目不难，关注题目解释中的判断AC条件
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

if __name__ == '__main__':
    Solution.removeDuplicates(11,[1,1,2])