def solution(arr):
    cnt = 0

    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 3]))