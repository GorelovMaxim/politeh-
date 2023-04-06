from math import log10


def calc_size(num):
    return int(log10(num) + 1)


def take(num, k):
    return num // (10 ** k) % 10


def solution(num):
    if num < 0:
        return False
    start = 0
    end = calc_size(num) - 1

    while start < end:
        if take(num, start) != take(num, end):
            return False
        start += 1
        end -= 1
    return True


if __name__ == "__main__":
    print(solution(121))
