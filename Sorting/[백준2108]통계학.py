import sys
from collections import Counter

N = int(sys.stdin.readline())   # 수의 개수
nums = []                       # 수를 담을 리스트

for i in range(N):
    nums.append(int(sys.stdin.readline()))
    
nums.sort()                     # 오름차순으로 정렬


print(round(sum(nums) / N))     # 산술평균
print(nums[N // 2])             # 중앙값

temp = Counter(nums).most_common() # 최빈값을 찾기 위한 임시 변수
# 최빈값
if len(temp) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

print(nums[-1] - nums[0])       # 범위
