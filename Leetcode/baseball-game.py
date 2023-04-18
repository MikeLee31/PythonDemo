from typing import List


def calPoints(ops: List[str]) -> int:
    ans = []

    for i in range(len(ops)):
        if ops[i] == '+':
            ans.append(int(ans[-1])+int(ans[-2]))
        elif ops[i] == 'D':
            x = int(ans[-1])*2
            ans.append(str(x))
        elif ops[i] == 'C':
            ans.pop()
        else:
            ans.append(ops[i])
        sum = 0
        print(ans)
    for an in ans:
        sum = sum + int(an)
    return sum


if __name__ == '__main__':

    print(calPoints(["5", "2", "C", "D", "+"]))
    print(calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
