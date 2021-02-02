N, M = map(int, input().split())        # N: 배열 A의 크기, M: 배열 B의 크기
aArr = list(map(int, input().split()))  # 배열 A 입력
bArr = list(map(int, input().split()))  # 배열 B 입력

answer = aArr + bArr    # 배열을 합침
answer.sort()           # 오름차순으로 정렬

print(' '.join(map(str, answer)))
