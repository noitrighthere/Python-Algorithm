"""
프로그래머스 신규 아이디 추천
난이도: LV1
유형: 문자열
"""
# 1단계: 모든 대문자를 대응하는 소문자로 치환
def step1(new_id):
    temp = ''
    
    for s in new_id:
        temp += s.lower()
    
    return temp


# 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
def step2(new_id):
    temp = ''

    for s in new_id:
        if s.isalpha() or s.isdigit() or s == '-' or s == '_' or s == '.':
            temp += s
        else:
            pass
        
    return temp

# 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
def step3(new_id):

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    return new_id

# 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
def step4(new_id):

    if new_id[0] == '.':
        new_id = new_id[1:] if len(new_id) > 1 else '.'

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    return new_id

# 5단계: 빈 문자열이라면 "a"를 대입
def step5(new_id):

    if len(new_id) == 0:
        new_id += 'a'

    return new_id

# 6단계: 길이가 16자 이상, 첫 15개를 제외한 나머지 문자를 제거
def step6(new_id):

    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    return new_id

# 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
def step7(new_id):

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
    

def solution(new_id):
    answer = ''

    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    answer = new_id
    
    return answer
