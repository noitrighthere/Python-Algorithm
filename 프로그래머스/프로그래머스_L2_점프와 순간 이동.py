"""
프로그래머스 점프와 순간 이동
난이도: LV2
유형: 재귀
"""
def solution(n):
    ans = 0
    
    while n > 0:

        # div: 몫, mod: 나머지
        div, mod = divmod(n, 2)

        # 나머지가 1일 때 +1
        if mod == 1:
            ans += 1

        n = div

    return ans
