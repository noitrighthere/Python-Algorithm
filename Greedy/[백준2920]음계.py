s = list(map(int, input().split(' ')))   # 음계 입력

ascending = True
descending = True

for i in range(1, 8):
    # 오름차순이면 descending은 False
    if s[i] > s[i-1]:
        descending = False
    # 내림차순이면 ascending은 False
    elif s[i] < s[i-1]:
        ascending = False

if ascending:
    print('ascending')
elif descending:
    print('descending')
else:
    print('mixed')
