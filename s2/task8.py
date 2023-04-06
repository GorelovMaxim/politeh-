def solution(s: str) -> bool:
    stack = []
    d = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    st = set(d.values())

    for i in s:
        if i in d:
            if len(stack) == 0 or stack[-1] != d[i]:
                return False
            stack.pop()
        elif i in st:
            stack.append(i)
    return len(stack) == 0


if __name__ == "__main__":
    print(solution("(a [b c {(x q b)}] d r)"))
