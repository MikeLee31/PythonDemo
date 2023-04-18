def selfDividingNumbers(left: int, right: int):
    ans = []
    for i in range(left, right + 1):
        if isDivid(i):
            ans.append(i)
    return ans


def isDivid(num):
    s = str(num)
    if s.find('0') != -1:
        return False
    for ss in s:
        if num % int(ss) != 0:
            return False
    return True


if __name__ == '__main__':
    print(selfDividingNumbers(1, 22))

