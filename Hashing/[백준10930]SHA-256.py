import hashlib

S = input()     # 문자열 S 입력
answer = hashlib.sha256(S.encode()) # sha256으로 인코딩

print(answer.hexdigest())           # 인코딩한 hex값 출력
