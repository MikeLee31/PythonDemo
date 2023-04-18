def trailingZeroes( n: int) -> int:
    sum = 1
    for i in range(1,n+1):
        sum*=i
    print(sum)
    s = str(sum)
    s = s[::-1]
    count=0
    for i in range(len(s)):
        if s[i]=='0':
            count=count+1
        else:
            break
    return count




if __name__ == '__main__':
    print(trailingZeroes(7))