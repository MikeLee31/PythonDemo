"""
使用教程
依次输入当前已有的物品数量
如我当前有
螺栓25木板24胶带25
则会计算出最均衡的所需数量
27螺栓27木板26胶带
-------------------
请输入第1个数字:25
请输入第2个数字:24
请输入第3个数字:25
平均加点--
[26, 27, 26] 79
推荐加点--
[27, 27, 26] 80
---------------------
"""


def calAve():
    nums = []
    sum = 80
    for i in range(3):
        nums.append(int(input(f"请输入第{i + 1}个数字:")))
        sum = sum + nums[i]
    ave = sum / 3
    sum = 0
    for i in range(3):
        nums[i] = int(ave - nums[i])
        sum = sum + nums[i]
    print("平均加点--")
    print(nums, sum)
    for i in range(80 - sum):
        ind = nums.index(min(nums))
        nums[ind] = nums[ind] + 1
        sum = sum + 1
    print("推荐加点--")
    print(nums, sum)


if __name__ == '__main__':
    calAve()
