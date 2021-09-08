"""
프로그래머스 전화번호 목록
난이도: LV2
유형: 해시
"""
phone_book = ["123","456","789"]

def solution(phone_book):
    answer = True
    hash_map = {}

    for number in phone_book:
        hash_map[number] = 1

    for number in phone_book:
        temp = ""
        for num in number:
            temp += num
            if temp in hash_map and temp != number:
                answer = False
    return answer

print(solution(phone_book))
