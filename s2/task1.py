def max_seq(arr):
    cur_neg = 0
    cur_pos = 0

    max_neg = 0
    max_pos = 0

    for num in arr:
        if num > 0:
            cur_pos += 1
            cur_neg = 0
        elif num < 0:
            cur_neg += 1
            cur_pos = 0
        else:
            cur_pos = 0
            cur_neg = 0
        max_neg = max(max_neg, cur_neg)
        max_pos = max(max_pos, cur_pos)
    return max(max_neg, max_pos)


if __name__ == "__main__":
    print(max_seq([1, 0, 3, -1, -2, 1]))
