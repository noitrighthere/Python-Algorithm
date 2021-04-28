def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 둘 중 하나라도 '1'이면 '1', 둘다 '0'이면 '0'
        temp = bin(arr1[i] | arr2[i])[2:]
        answer.append(("0" * (n-len(temp)) + temp).replace("1", "#").replace("0", " "
))
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))
