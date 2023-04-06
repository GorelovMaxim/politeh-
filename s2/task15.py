def rec(nums: list[int], res: list[list[int]], ans: list[int], cur: int):
    if len(ans) > 0:
        res.append(ans[:])
    for i in range(cur, len(nums)):
        ans.append(nums[i])
        rec(nums, res, ans, i + 1)
        ans.pop()


def solution(nums: list[int]):
    res = []
    rec(nums, res, [], 0)
    return res


if __name__ == "__main__":
    print(solution([1, 2, 3]))
