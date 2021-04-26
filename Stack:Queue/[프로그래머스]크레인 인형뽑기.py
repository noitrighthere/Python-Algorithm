def solution(board, moves):
    answer = 0      # 결과값
    stack = []      # 스택 생성

    for i in moves:
        for j in range(len(board)):
            # 크레인 위치에 따라 인형을 스택에 넣음
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                # 뽑은 인형위치는 0으로 표시
                board[j][i-1] = 0

                # 바구니에 인형이 생기면 해당 조건문 실행
                if len(stack) > 1:
                    # 같은 모향의 인형이 있으면 없앰
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer += 2

                break
        
    return answer
