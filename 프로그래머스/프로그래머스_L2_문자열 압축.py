"""
프로그래머스 문자열 압축
난이도: LV2
유형: 문자열
"""
def solution(s):
    answer = 0
    result = []
    string = ""

    # 문자열의 길이가 1이라면 1을 리턴
    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        count = 1
        temp = s[:i]

        # 문자열을 단위별로 확인
        for j in range(i, len(s), i):
            if s[j:j+i] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                string += str(count) + temp
                temp = s[j:j+i]
                count = 1

        if count == 1:
            count = ""
        string += str(count) + temp
        result.append(len(string))
        string = ""

    answer = min(result)
        
    return answer
