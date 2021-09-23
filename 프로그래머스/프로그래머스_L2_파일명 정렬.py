"""
프로그래머스 파일명 정렬
난이도: LV2
유형: 문자열
"""
import re

files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]

def solution(files):

    # 정규식 표현으로 숫자를 기준으로 나눈다
    answer = [re.split(r"([0-9]+)", s) for s in files]
    # 람다함수를 사용하여 대소문자, 숫자를 정렬
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in answer]

print(solution(files))
