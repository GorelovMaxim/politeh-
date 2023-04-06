def isNotBlank (myString):
    return bool(myString and myString.strip())

def evalution(s: str) -> int:
    stack = []
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x // y,
        '*': lambda x, y: x * y,
    }

    lexems = list(filter(isNotBlank, s.split(" ")))

    for i in lexems:
        if i in d:
            a = stack.pop()
            b = stack.pop()

            res = d[i](b, a)
            stack.append(res)
        else:
            stack.append(int(i))
    return stack.pop()

if __name__ == "__main__":
    print(evalution("5  6 + 3 * 22 -"))
