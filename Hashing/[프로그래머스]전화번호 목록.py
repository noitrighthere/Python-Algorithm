def solution(phone_book):

    # 접두어를 찾기 위해 오름차순으로 정렬함
    phone_book = sorted(phone_book)

    # zip()함수로 
    for x, y in zip(phone_book, phone_book[1:]):
        # 접두어인지 확인
        if y.startswith(x):
            return False

        return True
