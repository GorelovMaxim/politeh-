def solution(s):
    d = {}
    res = []

    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in sorted(d, key=lambda x: d[x], reverse=True):
        res.append(i * d[i])
    return "".join(res)


if __name__ == "__main__":
    print(solution("барракуда"))
