"""
프로그래머스 숫자 문자열과 영단어
난이도: LV1
유형:
"""
# 숫자를 판별하는 함수
def check(string):
    if string == "zero":
        return '0'
    elif string == "one":
        return '1'
    elif string == "two":
        return '2'
    elif string == "three":
        return '3'
    elif string == "four":
        return '4'
    elif string == "five":
        return '5'
    elif string == "six":
        return '6'
    elif string == "seven":
        return '7'
    elif string == "eight":
        return '8'
    elif string == "nine":
        return '9'
    else:
        return "n"

def solution(s):
    answer = ''

    temp = []   # 숫자 문자열을 담을 배열
    string = ''
    
    for data in s:
        # 문자가 숫자인 경우
        if data.isdigit():
            temp.append(int(data))
        # 영단어인 경우
        else:
            string += data
            if check(string).isdigit():
                temp.append(int(check(string)))
                string = ''
            else:
                continue
             
    for i in temp:
        answer += str(i)
      
    return int(answer)
