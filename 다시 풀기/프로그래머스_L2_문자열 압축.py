"""
프로그래머스 문자열 압축
난이도: LV2
유형: 문자열
"""

s = "aabbaccc"

def solution(s):
    answer = 0
    result = []

    if len(s) == 1:
        return 1

    for i in range(1, (len(s)//2)+1):
        string = ''
        cnt = 1
        temp = s[:i]

        for j in range(i, len(s), i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                string = string + temp
            temp = s[j:j+i]
            cnt = 1

    if cnt != 1:
        string = string + str(cnt) + temp
    else:
        string = string + temp

    result.append(len(string))
    answer = min(result)            
        
    return answer

print(solution(s))
