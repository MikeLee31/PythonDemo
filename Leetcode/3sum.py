from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums = sorted(nums)
#         print(nums)
#         answer = []
#         k = len(nums)
#         for i in range(0, k):
#             for j in range(i + 1, k):
#                 for l in range(j + 1, k):
#                     num1 = nums[i]
#                     num2 = nums[j]
#                     num3 = nums[l]
#                     if num1 + num2 + num3 == 0:
#                         for numlist in answer:
#                             if numlist.count(num1)!=0:
#                                 print("找到1")
#                                 if numlist.count(num2) != 0:
#                                     print("找到2")
#                                     if numlist.count(num3) != 0:
#                                         print("找到3")
#                                         continue
#                         l=[]
#                         l.append(num1)
#                         l.append(num2)
#                         l.append(num3)
#                         answer.append(l)
#         return answer

def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    # 如果空或者传入列表元素小于三
    if (not nums or n < 3):
        return []
    nums.sort()

    for i in range(n):
        # 已排序，第一个元素一定要小于0
        if (nums[i] > 0):
            return res
        # 前后元素相同跳过
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        # 双向扫描列表
        L = i + 1
        R = n - 1
        while (L < R):
            if (nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])
                # 如果元素相同则移动对于指针
                while (L < R and nums[L] == nums[L + 1]):
                    L = L + 1
                while (L < R and nums[R] == nums[R - 1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            # 如果大于0则移动右指针
            elif (nums[i] + nums[L] + nums[R] > 0):
                R = R - 1
            # 如果小于0移动左指针
            else:
                L = L + 1
    return res


if __name__ == '__main__':
    l = [-1, 0, 1, 2, -1, -4]
    print(threeSum(l))
