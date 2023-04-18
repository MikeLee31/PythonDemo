def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    else:
        maxx = 1
        for i in range(len(s)):
            d = {}
            count = 0
            j = i
            while j < len(s):
                try:
                    d[s[j]] = d[s[j]] + 1
                except:
                    d.update({s[j]: 1})
                if d[s[j]] == 2:
                    maxx = max(maxx, count)
                    break
                else:
                    count = count + 1
                    j = j + 1
            maxx = max(maxx, count)
        return maxx


if __name__ == '__main__':
    q = lengthOfLongestSubstring("hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789hijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    print(q)
