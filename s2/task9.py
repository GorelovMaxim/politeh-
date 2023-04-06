def lre(s: str) -> str:
    res = []

    i = 0
    while i < len(s):
        start = i
        while i + 1 < len(s) and s[i + 1] == s[i]:
            i += 1
        if start == i:
            res.append(s[i])
        else:
            res.append(f'@{i - start + 1}{s[i]}')
        i += 1
    return "".join(res)


if __name__ == "__main__":
    print(lre("XXXZZRRVBVVVVVWW"))
