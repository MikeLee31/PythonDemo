def uniqueMorseRepresentations(words) -> int:
    dirr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
            ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    ans = []
    for s in words:
        mos_str = ""
        for ss in s:
            mos_str = mos_str + dirr[ord(ss) - ord('a')]
        ans.append(mos_str)
    ans = set(ans)
    return len(ans)

if __name__ == '__main__':
    print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))