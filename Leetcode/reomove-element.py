def removeElement(nums, val: int) -> int:
    while nums.count(val) != 0:
        nums.remove(val)

    return len(nums)


if __name__ == '__main__':
    x = removeElement([3, 2, 2, 3], 3)
    print(x)
