

def lre(s: str) -> str:
    res = []

    i = 0
    while i < len(s):
        if s[i] != '@':
            res.append(s[i])
            i += 1
        else:
            res.append(s[i+2] * int(s[i+1]))
            i += 3
    return "".join(res)

if __name__ == "__main__":
    print(lre("@3X@2Z@2RVB@5V@2W"))