"""
프로그래머스 직업군 추천하기
난이도: LV1
유형: 정렬
"""
def solution(table, languages, preference):
    # 딕셔너리 생성
    dic = {}
    
    for lang, score in zip(languages, preference):
        dic[lang] = score

    scores = []

    for record in table:
        # 임시 변수를 만들어 기록을 나눔
        split_record = record.split(' ')
        sum_score = 0

        for lang in languages:
            # 언어가 임시 변수에 있으면
            if lang in split_record:
                # 점수를 만듬
                score = 6 - split_record.index(lang)
                # 점수 계산
                sum_score += score * dic[lang]

        scores.append(sum_score)

    # 제일 큰 점수를 담을 임시 배열
    temp = []
    for index, score in enumerate(scores):
        if score == max(scores):
            temp.append(table[index].split()[0])

    # 같은 값의 점수가 있을 때 단어순으로 정렬
    temp.sort()
    
    answer = temp[0]
    return answer
