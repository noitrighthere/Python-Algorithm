def solution(strings, n):
    # 한 번 오름차순으로 정렬 후, 인덱스 값에 맞게 다시 오름차순으로 정렬
    return sorted(sorted(strings), key=lambda x: x[n])
