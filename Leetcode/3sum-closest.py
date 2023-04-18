def threeSumClosest(nums, target: int) -> int:
    n = len(nums)
    res = []
    # 如果空或者传入列表元素小于三
    if (not nums or n < 3):
        return []
    nums.sort()
    small = 999999
    for i in range(n):
        # 已排序，第一个元素一定要小于0
        # 前后元素相同跳过

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 双向扫描列表
        L = i + 1
        R = n - 1
        while L < R:
            # 获得与目标差距
            target_sub = abs(nums[i] + nums[L] + nums[R] - target)
            # 差距变小了,更新
            if target_sub < small:
                small = target_sub
                res.clear()
                # 注意这里是嵌套列表[[1,2,3]]这种的
                res.append([nums[i], nums[L], nums[R]])

            # 因为数组排好序, 所以如果和比target大移动右指针可以使和变小
            if nums[i] + nums[L] + nums[R] > target:
                R = R - 1
            # 如果小于target移动左指针使和变大
            else:
                L = L + 1
    sum = 0
    # 所以遍历为res[0]
    for re in res[0]:
        sum = sum + re
    return sum


if __name__ == '__main__':
    # print(threeSumClosest([1,1,1,0], -100))
    print(threeSumClosest([0, 2, 1, -3], 1))
