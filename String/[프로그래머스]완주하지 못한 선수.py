def solution(participant, completion):

   participant.sort()   # 참가한 선수 정렬
   completion.sort()    # 완주한 선수 정렬

   # zip함수를 사용하여 둘의 일치여부 판단
   for temp_p, temp_c in zip(participant, completion):

       # 완주하지 못한 선수를 찾음
       if temp_p != temp_c:
           return temp_p

    # 중복된 값이 있다면 맨 마지막에 중복된 값이 나옴
    return participant[-1]
