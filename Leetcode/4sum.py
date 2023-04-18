# def fourSum(nums, target: int):
#     nums.sort()
#     le = len(nums)
#     answer = []
#     for i in range(le):
#         for j in range(i + 1, le):
#             pre_sum = nums[i] + nums[j]
#             if (i > 0 and nums[i] == nums[i - 1]):
#                 continue
#             l = j + 1
#             r = le - 1
#             while (l < r):
#                 if nums[l] + nums[r] + pre_sum < target:
#                     l = l + 1
#                 elif nums[l] + nums[r] + pre_sum > target:
#                     r = r - 1
#                 else:
#                     ans = []
#                     ans.append(nums[i])
#                     ans.append(nums[j])
#                     ans.append(nums[l])
#                     ans.append(nums[r])
#                     flag = False
#                     for a in answer:
#                         if IsSame(ans, a):
#                             flag = True
#                     if not flag:
#                         answer.append(ans)
#                     l = l + 1
#                     r = r - 1
#     return answer
#
#
# def IsSame(list1, list2):
#     for i in range(3):
#         if list1[i] != list2[i]:
#             return False
#     return True

def fourSum(nums, target: int):
    n = len(nums)
    res = []
    nums.sort()
    if not nums or n < 4:
        return []
    for i in range(n):
        for j in range(i + 1, n):
            pre_sum = nums[i] + nums[j]
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = j + 1
            R = n - 1
            while (L < R):
                if nums[L] + nums[R] + pre_sum < target:
                    L += 1
                elif nums[L] + nums[R] + pre_sum > target:
                    R -= 1
                else:
                    re = []
                    re.append([nums[i], nums[j], nums[L], nums[R]])
                    # re.append(nums[i])
                    # re.append(nums[j])
                    # re.append(nums[L])
                    # re.append(nums[R])
                    flag = False
                    for a in res:
                        if IsSame(re, a):
                            flag = True
                        if not flag:
                            res.append(re)
                        L += 1
                        R -= 1
        return res

def IsSame(list1, list2):
    for i in range(3):
        if list1[i] != list2[i]:
            return False
    return True


if __name__ == '__main__':
    # print(fourSum([1,-2,-5,-4,-3,3,3,5],-11))
    print(fourSum([1,0,-1,0,-2,2], 0))
# [1,-2,-5,-4,-3,3,3,5],-11










