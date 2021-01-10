def solution(arr):

    # 배열의 크기가 1보다 클때
    if len(arr) > 1:
        # 가장 작은 배열 값 제거
        arr.remove(min(arr))
        return (arr)
    else:
        return [-1]
