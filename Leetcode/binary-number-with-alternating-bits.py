def hasAlternatingBits( n: int) -> bool:
    s=[]
    x = n
    if x % 2 == 1:
        s.append('1')
    else:
        s.append('0')
    while x!=1:
        x = int(x/2)
        if x%2==1:
            s.append('1')
        else:
            s.append('0')
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            return False
    return True


if __name__ == '__main__':
    print(hasAlternatingBits(7))
    print(hasAlternatingBits(5))
    print(hasAlternatingBits(11))


