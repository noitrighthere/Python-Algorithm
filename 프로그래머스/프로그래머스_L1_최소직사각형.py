"""
프로그래머스 최소직사각형
난이도: LV1
유형: 구현
"""
def solution(sizes):
    width, height = 0, 0
    for w, h in sizes:
        width, height = max(width, w, h), max(height, min(w, h))

    answer = width * height
    
    return answer
